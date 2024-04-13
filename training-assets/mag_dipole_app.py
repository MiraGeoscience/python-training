#!/usr/bin/env python

from __future__ import annotations

import sys

import numpy as np
from geoh5py.data import Data
from geoh5py.objects import ObjectBase
from geoh5py.ui_json import InputFile
from geoh5py.ui_json.utils import monitored_directory_copy


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

    # mu_0 / 4 pi  * 1e9 for nT
    constant = 100
    fields = constant * (
        ((np.dot(m, rad.T).T * 3 * rad) / dist[:, None] ** 5) - (m / dist[:, None] ** 3)
    )

    return fields


def inclination_declination_2_xyz(inclination, declination):
    """Convert inclination and declination angles (degrees) to unit vector (xyz)."""
    theta = np.deg2rad((450 - declination) % 360)
    phi = np.deg2rad(90 + inclination)
    xyz = np.c_[np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)]

    return xyz


def tmi_projection(b_components, earth_field):
    """Project magnetic field onto Earth's field."""
    h0 = inclination_declination_2_xyz(earth_field[0], earth_field[1])
    return np.dot(h0, b_components.T)


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
    :param earth_inc: Earth's field inclination angle.
    :param earth_dec: Earth's field declination angle.

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


if __name__ == "__main__":
    file = sys.argv[1]
    run(file)


#  Copyright (c) 2022 Mira Geoscience Ltd.
