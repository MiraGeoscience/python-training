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
    ifile = InputFile(file)
    fields = dipole_simulation(
        ifile["dipoles"],
        ifile["locations"],
        ifile["moments"],
        ifile["azimuths"],
        ifile["dips"],
    )

    with ifile["geoh5"].open(mode="r+"):
        ifile["locations"].add_data(
            {
                "b_x": {"values": fields[:, 0]},
                "b_y": {"values": fields[:, 1]},
                "b_z": {"values": fields[:, 2]},
            }
        )

        if ifile["monitoring_directory"] is not None:
            monitored_directory_copy(ifile["monitoring_directory"], ifile["locations"])

        # point.add_data(
        #     {
        #         "moment": {"values": np.r_[moment]},
        #         "azimuth": {"values": np.r_[azimuth]},
        #         "dip": {"values": np.r_[dip]},
        #     }
        # )


def dipole_simulation(
    dipoles: np.ndarray | Points,
    locations: np.ndarray | ObjectBase,
    moments: Data | float,
    azimuths: Data | float,
    dips: Data | float,
):
    """
    Compute the magnetic field components of dipoles on a geoh5py object.

    :param dipoles: Array or Points object of dipole locations, shape(m, 3).
    :param locations: Array or Points object of observation locations, shape(n, 3).
    :param moments: Value or Data of dipole moments.
    :param azimuths: Value or Data of dipole azimuth angles.
    :param dips: Value or Data of dipole dip angles.

    :return b_field: Vector array of magnetic field components, shape(n ,3).
    """
    sources = dipoles
    if isinstance(dipoles, Points):
        sources = dipoles.vertices

    receivers = locations
    if isinstance(receivers, ObjectBase):
        if hasattr(receivers, "centroids"):
            receivers = locations.centroids
        else:
            receivers = locations.vertices

    n_rec = receivers.shape[0]
    if isinstance(moments, Data):
        moments = moments.values
    else:
        moments = np.ones(n_rec) * moments

    if isinstance(azimuths, Data):
        azimuths = azimuths.values
    else:
        azimuths = np.ones(n_rec) * azimuths

    if isinstance(dips, Data):
        dips = dips.values
    else:
        dips = np.ones(n_rec) * dips

    fields = np.zeros_like(locations)

    for source, moment, azimuth, dip in zip(sources, moments, azimuths, dips):
        fields += b_field(source, receivers, moment, azimuth, dip)

    return fields


def b_field(source, locations, moment, azimuth, dip):
    """
    Compute the magnetic field components of a dipole on an array of locations.


    """
    theta = np.deg2rad((450 - azimuth) % 360)
    phi = np.deg2rad(90 + dip)
    m = (
        moment
        * np.c_[np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)]
    )
    delta = source - locations
    radius = np.sum(delta**2.0, axis=1) ** 0.5
    fields = (np.dot(m, delta.T).T * delta) / radius[:, None] ** 4.0 - np.repeat(
        m, locations.shape[0]
    ).reshape((-1, 3), order="F") / radius[:, None] ** 3.0

    return fields


if __name__ == "__main__":
    file = sys.argv[1]
    run(file)

#  Copyright (c) 2022 Mira Geoscience Ltd.
