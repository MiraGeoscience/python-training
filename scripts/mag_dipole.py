from __future__ import annotations

import sys

import numpy as np
from geoh5py.data import Data
from geoh5py.objects import ObjectBase, Points
from geoh5py.ui_json import InputFile
from geoh5py.ui_json.utils import monitored_directory_copy


def run(file: str):
    """
    Run the mag_dipole simulation from InputFile.
    """
    ifile = InputFile.read_ui_json(file).data
    MagneticSimulation(
        ifile["sources"],
        ifile["receivers"],
        ifile["moments"],
        ifile["inclination"],
        ifile["declination"],
    ).run()

    with ifile["geoh5"].open(mode="r+"):

        if ifile["monitoring_directory"] is not None:
            monitored_directory_copy(ifile["monitoring_directory"], ifile["receivers"])


class MagneticSimulation:
    """
    Compute the magnetic field components of dipoles on a geoh5py object.

    :param dipoles: Array or Points object of dipole locations, shape(m, 3).
    :param locations: Array or Points object of observation locations, shape(n, 3).
    :param moments: Value or Data of dipole moments.
    :param inclinations: Value or Data of dipole inclination angles.
    :param declinations: Value or Data of dipole declination angles.

    :return b_field: Vector array of magnetic field components, shape(n ,3).
    """

    def __init__(
        self,
        sources: Points,
        receivers: ObjectBase,
        moments: Data | float,
        inclinations: Data | float,
        declinations: Data | float,
        earth_field=(90.0, 0),
    ):
        self._sources = sources
        self._receivers = receivers
        self._moments = moments
        self._inclinations = inclinations
        self._declinations = declinations
        self._earth_field = earth_field

    @property
    def sources(self):
        if hasattr(self._sources, "centroids"):
            return self._sources.centroids
        return self._sources.vertices

    @property
    def receivers(self):
        if hasattr(self._receivers, "centroids"):
            return self._receivers.centroids
        return self._receivers.vertices

    @property
    def moments(self):
        if isinstance(self._moments, Data):
            return self._moments.values
        if isinstance(self._moments, float):
            return np.ones(self.sources.shape[0]) * self._moments

        return self._moments

    @property
    def inclinations(self):
        if isinstance(self._inclinations, Data):
            return self._inclinations.values
        if isinstance(self._inclinations, float):
            return np.ones(self.sources.shape[0]) * self._inclinations

        return self._inclinations

    @property
    def declinations(self):
        if isinstance(self._declinations, Data):
            return self._declinations.values
        if isinstance(self._declinations, float):
            return np.ones(self.sources.shape[0]) * self._declinations

        return self._declinations

    def compute(self):
        """Compute fields from input."""
        fields = np.zeros_like(self.receivers)

        for source, moment, inclination, declination in zip(
            self.sources, self.moments, self.inclinations, self.declinations
        ):
            fields += b_field(source, self.receivers, moment, inclination, declination)

        return fields

    def tmi_projection(self, fields):
        """Project magnetic field onto Earth's field."""
        H = inclination_declination_2_xyz(
            self._earth_field[0], self._earth_field[1]
        )  # Suncity field parameters
        return np.dot(H, fields.T)

    def run(self):
        """Run the simulation and save."""
        with self._receivers.workspace.open(mode="r+"):
            fields = self.compute()
            tmi = self.tmi_projection(fields)
            data = self._receivers.add_data(
                {
                    "b_x": {"values": fields[:, 0]},
                    "b_y": {"values": fields[:, 1]},
                    "b_z": {"values": fields[:, 2]},
                    "tmi": {"values": tmi},
                }
            )

        return data


def inclination_declination_2_xyz(inclination, declination):
    """Convert inclination and declination angles (degrees) to unit vector (xyz)."""
    theta = np.deg2rad((450 - inclination) % 360)
    phi = np.deg2rad(90 + declination)
    xyz = np.c_[np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)]

    return xyz


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


if __name__ == "__main__":
    file = sys.argv[1]
    run(file)

#  Copyright (c) 2022 Mira Geoscience Ltd.
