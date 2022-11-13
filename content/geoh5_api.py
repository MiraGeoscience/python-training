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

# # Programming with `geoh5` (ANALYST API)
#
#
# This section provides examples on how to interact with Geoscience ANALYST
# programmatically by using the geoh5 API [geoh5py](https://geoh5py.readthedocs.io/en/stable/)

# ## Open/create a Workspace
#
# The main element controlling the hierarchy of a `geoh5` is the `Workspace` class.
#
# First we need to import the API package to our active Python session.

from geoh5py.workspace import Workspace

# There are two ways to create or connect to an existing `geoh5` file.
#
# ### Option 1: Context manager
#
# The `Workspace` class can open a file as a context manager using the `with`
# statement. Just like any other [function](functions), everything after the `:`
# must be indented to be part of the scope. This is the **preferred** method to
# interact with the `geoh5` to make sure that the file gets closed at the end of
# the program, even if the program fails due to some error along the way.

with Workspace("my_file.geoh5") as workspace:
    print(workspace)

# ### Option 2: `open()` and `close()`
#
# The second option is to directly call the `open()` method of the Workspace class.
#
# ```
# workspace = Workspace("my_file.geoh5")
# ```

workspace = Workspace("my_file.geoh5").open()

# With this option, Python keeps a connection to the file until the `close()`
# method gets called. This is sometimes preferable if the computations take a
# long time or if you want to prevent other programs to access the file while your program is operating on it.

workspace.close()

# ## Creating objects
#
# The `geoh5` format supports a wide range of object types as [documented here](https://geoh5py.readthedocs.io/en/stable/content/geoh5_format/analyst/objects.html#analyst-objects). For this training, we will create a simple Grid2D object using the `.create()` method.

from geoh5py.objects import Grid2D

# For the grid to be fully defined, we need to assign some properties about its geometry.

with Workspace("my_file.geoh5") as workspace:
    grid = Grid2D.create(
        workspace,
        origin=[-32, -64, 0],  # South-west corner coordinates
        u_cell_size=1.0,  # Cell size along u-axis
        v_cell_size=1.0,  # Cell size along v-axis
        u_count=64,  # How many cells along u-axis
        v_count=128,  # How many cells along v-axis
    )

# Since we have created the grid within a context, you can now safely open the `my_file.geoh5` with ANALYST to see the grid that was created.
#
# ![grid2d](./images/grid2d.png)

# ## Generating Data
#
# Now that we have an object created, we can add data to it. We will borrow some functions from the `numpy` package to compute values on the cells of our 2D grid.

import numpy as np
from geoh5py.objects import Points

# ### Example 1: Electric field of a point charges
#
# Let's start with a simple problem of computing the electric field due to a
# collection of charges. From first year physics, the field of a single charge is:
#
# $$\frac{k Q}{r^2}$$
#
# where $k$ and $Q$ are some constants (don't worry about it) and $r$ is the
# distance between the charge and the observation point (our grid cells).
# We can first create a small function that computes the electric field for a single charge.
#
# ```
# def e_field(charge, location, grid):
#
#     radius = np.sum((locations - grid.centroids)**2., axis=1)**0.5
#     e_field = charge / r**2.
# ```


def e_field(charge, locations, grid):
    delta = locations - grid.centroids
    radius = np.sum(delta**2.0, axis=1) ** 0.5
    field = charge / radius**2.0

    return field


# We can now create some point charges and add up their collective fields. We will use the
#
# - `numpy.random` module to generate what we need
# - `numpy.zeros` module to create our initial array of e-field.

n_charges = 10
charges = np.random.randn(n_charges)
locations = np.random.randn(n_charges, 3) * 10.0
field = np.zeros(grid.n_cells)

# We can now loop over the charges and their respective locations, compute the field and add it up to our final array.

for charge, location in zip(charges, locations):
    field += e_field(charge, location, grid)

# We then add the total electric field to our Grid2D, as well as creating some Points to show where the charges were.

with workspace.open():
    grid.add_data({"e_field": {"values": field}})

    points = Points.create(workspace, vertices=locations)
    points.add_data({"charge": {"values": charges}})

# Et voila!
#
# ![efield](./images/e_field.png)

# For more examples on how to create other object types, visit the [geoh5py-Tutorial](https://geoh5py.readthedocs.io/en/stable/content/user_guide/core_entities.html#Entities)

#  Copyright (c) 2022 Mira Geoscience Ltd.
