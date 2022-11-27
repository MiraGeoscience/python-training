# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Magnetic Dipole App
#
# Now that we have learned how to interact with `geoh5` and to create a custom user-interface with `ui.json`, we can start implementing our first application. We are going to create a a magnetic dipole simulator from scratch, which could become a useful tool to interpret magnetic data maps.
#
#
# ![mag_dipole_gif](./images/mag_dipole_app.gif "segment")
#
#
# ## The physics
#
# From first year physics, the magnetic field of a single dipole is:
#
# $$\mathbf{B} = \frac{\mu_0}{4 \pi}  \frac{3 (\mathbf{m} \cdot \mathbf{r})  \mathbf{\hat r} - \mathbf{m}}{r^3}$$
#
# where $\mu_0$ is a constant ($4 \pi \times 1e-9$), $\mathbf{m}$ is the magnetic dipole and $\mathbf{r}$ is the
# vector separating the dipole and the observations.
#
# In a mineral exploration context however, we normally get Total
# Magnetic Intensity (TMI) data from magnetometers. The conversion can be
# approximated by a projection of the fields onto the direction of Earth's inducing field.
#
# $$
# b_{TMI} \approx \mathbf{\hat H}_0 \cdot \mathbf{b}
# $$
#
# So we will need at least to
#  - Create functions for:
#     - Computing the fields of a dipole(s)
#     - Converting vector fields to TMI.
#  - Provide inputs for parameters:
#     - Receivers (observation) locations
#     - Source dipole locations
#     - Dipole moment values
#     - Dipole inclination angles
#     - Dipole declination angles
#     - Earth's field inclination
#     - Earth's field declination
#
# Let's get on with it.


# Import the necessary packages
from __future__ import annotations
import json
import matplotlib.pyplot as plt
import numpy as np
from geoh5py.data import Data
from geoh5py.objects import ObjectBase, Points
from geoh5py.ui_json import InputFile, constants, templates
from geoh5py.ui_json.utils import monitored_directory_copy
from geoh5py.workspace import Workspace

# ## The functions
#
# We can begin with writing the function needed to compute the
# magnetic field from a single dipole. The function should be able to take as argument
#
#     - Coordinates of the source and receivers (defining $\mathbf{r}$),
#     - Parameters defining the strength (moment) and orientation (inc, dec) of the dipole source.

# + tags=["clear-form"]
def b_field(source, locations, moment, inclination, declination):
    """
    Compute the magnetic field components of a dipole on an array of locations.

    :param source: Location of a point dipole, shape(1, 3).
    :param locations: Array of observation locations, shape(n, 3).
    :param moment: Dipole moment of the source (A.m^2)
    :param inclination: Dipole horizontal angle, clockwise from North
    :param declination: Dipole vertical angle from horizontal, positive down

    :return: Array of magnetic field components, shape(n, 3)
    """
    # Convert the inclination and declination to Cartesian vector
    m = moment * inclination_declination_2_xyz(inclination, declination)

    # Compute the radial components
    rad = source - locations

    # Compute |r|
    dist = np.sum(rad**2.0, axis=1) ** 0.5

    # mu_0 / 4 pi * 1e-9 (nano)
    constant = 1e2
    fields = (
        constant
        * ((np.dot(m, rad.T).T * (rad / dist[:, None])) - m)
        / dist[:, None] ** 3.0
    )

    return fields


# -

# We have made use a few useful methods on `numpy` arrays.
# - The `sum()` method applied to a specific axis of an array, collapsing the dimension.
# - The `dot()` method performs the dot product between two arrays
# - The transpose (`.T`) method to get the dimensions of arrays to align:
#
# $[1 \times 3] \cdot [M \times 3].T \rightarrow [1 \times M] $.
#
# - Array broadcasting (repeat) of a 1D array along a second dimension using the `[:, None]` indexing:
#
# $[N \times 3] \;/\;([1 \times N][: None]) \rightarrow [N \times 3] $
#
#
# Looks like we might also need a small function to convert inclination/declination angles to Cartesian vectors. The same function will come handy later when computing the TMI projection.


def inclination_declination_2_xyz(inclination, declination):
    """Convert inclination and declination angles (degrees) to unit vector (xyz)."""
    theta = np.deg2rad((450 - declination) % 360)
    phi = np.deg2rad(90 + inclination)
    xyz = np.c_[np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)]

    return xyz


# We can now test our `b_field` function with existing objects present in our `suncity.geoh5` project.

# + tags=["clear-form"]
with Workspace("../assets/suncity.geoh5") as workspace:
    points = workspace.get_entity("Points")[0]
    grid = workspace.get_entity("SunCity")[0]
    vector_b = b_field(points.vertices[0, :], grid.centroids, 1.0, 90, 0)


# -

# The `b_field` function returns an array for the three components of the
# magnetic field due to the dipole source.
#
# Let's write a simple function to get the TMI (projected) data instead.


def tmi_projection(b_components, earth_field):
    """Project magnetic field onto Earth's field."""
    h0 = inclination_declination_2_xyz(earth_field[0], earth_field[1])
    return np.dot(h0, b_components.T)


# and test it for the inducing field parameters at our test site at Suncity `(Inc: -62.11, Dec: -17.9)`.

# + tags=["clear-form"]
tmi_b = tmi_projection(vector_b, (-62.11, -17.9))
# -

# ## The Simulator
#
# In this section, we are going to string together the functions defined above and generalize our approach so that we can deal with different types of `geoh5` objects. Let's wrap all the previous functions into a `magnetic_simulator` class.


# + tags=["clear-form"]
def magnetic_simulator(
    sources: ObjectBase,
    receivers: ObjectBase,
    moments: Data | float,
    inclinations: Data | float,
    declinations: Data | float,
    earth_inc: float,
    earth_dec: float,
):
    """
    Compute the magnetic field components of dipoles on a geoh5py object.

    :param sources: Points object of dipole locations.
    :param receivers: Array or Points object of observation locations.
    :param moments: Value or Data of dipole moments.
    :param inclinations: Value or Data of dipole inclination angles.
    :param declinations: Value or Data of dipole declination angles.

    :return b_field: List of Data entities.
    """

    def locations(entity):
        if hasattr(entity, "centroids"):
            return entity.centroids

        return entity.vertices

    # Extract dipole coordinates
    dipoles = locations(sources)

    # Extract receiver coordinates
    observations = locations(receivers)

    def vectorize(entity):
        if isinstance(entity, Data):
            return entity.values

        return np.ones(dipoles.shape[0]) * entity

    # Get dipole moment values
    mom = vectorize(moments)
    # Get dipole inclination values
    inc = vectorize(inclinations)
    # Get dipole declination values
    dec = vectorize(declinations)

    # Loop over the dipoles
    fields = np.zeros_like(observations)

    for source, moment, inclination, declination in zip(dipoles, mom, inc, dec):
        fields += b_field(source, observations, moment, inclination, declination)

    tmi = tmi_projection(fields, (earth_inc, earth_dec))

    # Add data to receiver object
    data = receivers.add_data(
        {
            "b_x": {"values": fields[:, 0]},
            "b_y": {"values": fields[:, 1]},
            "b_z": {"values": fields[:, 2]},
            "tmi": {"values": tmi},
        }
    )

    return data


# -

# We now have a generic container to compute TMI data based on any type of ANALYST object.
#
# You are now invited to edit your Points object to add more vertices and
# create data arrays for moment, azimuth and dips. We can now run the simulation
# by simply giving those entities to our class.

# + tags=["clear-form"]
with workspace.open(mode="r+"):
    magnetic_simulator(points, grid, 1.0, 90.0, 0.0, -62.11, -17.9)


# -

# ![bfield](./images/b_field.png)

# ## The Driver
#
# In the previous, we created our simulation program called `magnetic_simulator` that could compute the fields of dipoles defined by `geoh5` object. As a final step, we need to define a `driver` program that can be called from ANALYST.
#
# We are going to take advantage of the
# [geoh5py.ui_json.InputFile](https://geoh5py.readthedocs.io/en/stable/content/api/geoh5py.ui_json.html#geoh5py.ui_json.input_file.InputFile)
# class to handle value conversions between geoh5 and python, as well as the `monitored_directory_copy` function to handle the live link with ANALYST.

# + tags=["clear-form"]
def run(file: str):
    """
    Run the mag_dipole simulation from InputFile.
    """
    ifile = InputFile.read_ui_json(file).data

    with ifile["geoh5"].open(mode="r+"):
        magnetic_simulator(
            ifile["sources"],
            ifile["receivers"],
            ifile["moments"],
            ifile["inclination"],
            ifile["declination"],
            ifile["earth_inc"],
            ifile["earth_dec"],
        )

        if ifile["monitoring_directory"] is not None:
            monitored_directory_copy(ifile["monitoring_directory"], ifile["receivers"])


# -

# The final step requires to make this program available to python to be executed from ANALYST.
#
# Do the following:
#
# - Use the `File\Download as\Python *.py` dropdown menu to convert this notebook to a `py` file.
# - Rename the file to `mag_dipole_app.py`.
# - Remove everything in the file except the
#     - the imports,
#     - the blocks of functions `def`
#     - the following lines (without #'s)
#
#     ```
#     if __name__ == "__main__":
#         file = sys.argv[1]
#         run(file)
#     ```
#
# This part becomes the entry point of the python interpreter when running the
# `mag_dipole_app.py` script. At the end, your file should look like this.
#
# ![run_command](./images/run_command.png)

# ## The User-Interface (ui.json)
#
# In the previous section covering the [geoh5 API](geoh5-API), we have introduced functionality to compute the magnetic field from dipole locations. We are now going to create a user-interface (UI) to be able to run this program from a Geoscience ANALYST session.
#
# We now can create our ui.json to provide inputs for the following 5 parameters:
#
# - `Object` defining the dipoles (sources)
# - `Object` defining the receivers
# - `Data` or `float` value for the dipole moments
# - `Data` or `float` value for the dipole inclination angles
# - `Data` or `float` value for the dipole declination angles
# - `Float` value for Earth's field inclination angle
# - `Float` value for Earth's field declination angle
#
# Let's create a UI.json with forms for each one of those inputs

# + tags=["clear-form"]
mag_ui = constants.default_ui_json.copy()
mag_ui["title"] = "Magnetic Dipole App"
mag_ui.update(
    {
        "sources": templates.object_parameter(label="Dipoles", mesh_type="", value=""),
        "receivers": templates.object_parameter(
            label="Receivers", mesh_type="", value=""
        ),
        "moments": templates.data_parameter(
            label="Dipole Moment", parent="sources", value=1.0
        ),
        "inclination": templates.data_parameter(
            label="Dipole Inclination", parent="sources", value=-62.11
        ),
        "declination": templates.data_parameter(
            label="Dipole Declination", parent="sources", value=-17.9
        ),
        "earth_inc": templates.data_parameter(
            label="Earth's field Inclination", parent="sources", value=-62.11
        ),
        "earth_dec": templates.data_parameter(
            label="Earth's field Declination", parent="sources", value=-17.9
        ),
    }
)


# Some modifications
for label in ["moments", "inclination", "declination"]:
    mag_ui[label]["isValue"] = True
    mag_ui[label]["property"] = ""
# -

# We now need tell which "program" that ANALYST can call.

# + tags=["clear-form"]
mag_ui["conda_environment"] = "python-training"
mag_ui["run_command"] = "mag_dipole_app"
# -

# Internally, when executed from ANALYST, this is what is going to happen
#
# ```
# conda activate python-training
# python mag_dipole
# ```
#
# Then your mag_dipole.run should be able to do the rest: compute and store the result.
#
# Let's write out our ui.json to file.

# + tags=["clear-form"]
with open("../assets/magnetic_dipole.ui.json", "w", encoding="utf-8") as file:
    json.dump(mag_ui, file, indent=4)
# -

#  Copyright (c) 2022 Mira Geoscience Ltd.
