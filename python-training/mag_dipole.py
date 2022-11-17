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
    ifile = InputFile(file).data
    MagneticSimulation(
        ifile["dipoles"],
        ifile["locations"],
        ifile["moments"],
        ifile["azimuths"],
        ifile["dips"],
    ).run()

    with ifile["geoh5"].open(mode="r+"):

        if ifile["monitoring_directory"] is not None:
            monitored_directory_copy(ifile["monitoring_directory"], ifile["locations"])


class MagneticSimulation:
    """
    Compute the magnetic field components of dipoles on a geoh5py object.

    :param dipoles: Array or Points object of dipole locations, shape(m, 3).
    :param locations: Array or Points object of observation locations, shape(n, 3).
    :param moments: Value or Data of dipole moments.
    :param azimuths: Value or Data of dipole azimuth angles.
    :param dips: Value or Data of dipole dip angles.

    :return b_field: Vector array of magnetic field components, shape(n ,3).
    """

    def __init__(
        self,
        sources: Points,
        receivers: ObjectBase,
        moments: Data | float,
        azimuths: Data | float,
        dips: Data | float,
        earth_field=(90.0, 0),
    ):
        self._sources = sources
        self._receivers = receivers
        self._moments = moments
        self._azimuths = azimuths
        self._dips = dips
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
    def azimuths(self):
        if isinstance(self._azimuths, Data):
            return self._azimuths.values
        if isinstance(self._azimuths, float):
            return np.ones(self.sources.shape[0]) * self._azimuths

        return self._azimuths

    @property
    def dips(self):
        if isinstance(self._dips, Data):
            return self._dips.values
        if isinstance(self._dips, float):
            return np.ones(self.sources.shape[0]) * self._dips

        return self._dips

    def compute(self):
        """Compute fields from input."""
        fields = np.zeros_like(self.receivers)
        for source, moment, azimuth, dip in zip(
            self.sources, self.moments, self.azimuths, self.dips
        ):
            fields += b_field(source, self.receivers, moment, azimuth, dip)

        return fields

    def tmi_projection(self, fields):
        """Project magnetic field onto Earth's field."""
        H = azimuth_dip_2_xyz(
            self._earth_field[0], self._earth_field[1]
        )  # Suncity field parameters
        return np.dot(H, fields.T)

    def run(self):
        """Run the simulation and save."""
        fields = self.compute()
        tmi = self.tmi_projection(fields)

        with self._receivers.workspace.open(mode="r+"):
            data = self._receivers.add_data(
                {
                    "b_x": {"values": fields[:, 0]},
                    "b_y": {"values": fields[:, 1]},
                    "b_z": {"values": fields[:, 2]},
                    "tmi": {"values": tmi},
                }
            )

        return data


def azimuth_dip_2_xyz(azimuth, dip):
    """Convert azimuth and dip angles (degrees) to unit vector (xyz)."""
    theta = np.deg2rad((450 - azimuth) % 360)
    phi = np.deg2rad(90 + dip)
    xyz = np.c_[np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)]

    return xyz


def b_field(source, locations, moment, azimuth, dip):
    """
    Compute the magnetic field components of a dipole on an array of locations.

    :param source: Location of a point dipole, shape(1, 3).
    :param locations: Array of observation locations, shape(n, 3).
    :param moment: Dipole moment of the source (A.m^2)
    :param azimuth: Dipole horizontal angle, clockwise from North
    :param dip: Dipole vertical angle from horizontal, positive down

    :return: Array of magnetic field components, shape(n, 3)
    """
    # Convert the azimuth and dip to Cartesian vector
    m = moment * azimuth_dip_2_xyz(azimuth, dip)

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
