# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming with `geoh5` (ANALYST API)
#
#
# This section provides examples on how to interact with Geoscience ANALYST
# programmatically by using the geoh5 API [geoh5py](https://geoh5py.readthedocs.io/en/stable/).
# We are going to demonstrate how to
#
# - Create/open a geoh5 workspace
# - Access objects and data
# - Use third-party packages to create and plot data
#
# Let's get started with some imports.

# +
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from geoh5py.objects import Points
from geoh5py.workspace import Workspace

from training import assets_path
# -

# ## Open/create a Workspace
#
# The main element controlling the hierarchy of a `geoh5` is the `Workspace`.
# It is the class responsible for accessing information on disk and to register
# and create the various entities (groups, objects, data).
#
# There are two ways to create or connect to an existing `geoh5` file through the `Workspace`.

# ### Option 1: Context manager
#
# The `Workspace` class can open a file as a context manager using the `with`
# statement. Just like any other [function](functions), everything after the `:`
# must be indented to be part of the scope. This is the **preferred** method to
# interact with the `geoh5` to make sure that the file gets closed at the end of
# the context, even if the code has to exit premarturely due to error.

# + tags=["clear-form"]
with Workspace(assets_path() / "suncity.geoh5") as workspace:
    print(workspace.geoh5)
# -

# ### Option 2: `open()` and `close()`
#
# The second option is to directly instantiate the Workspace or to call the `open()` method.

# + tags=["clear-form"]
workspace.open()
workspace.geoh5
# -

# With this option, Python keeps a connection to the file until the `close()`
# method gets called. This is sometimes preferable if the computations take a
# long time or if you want to prevent other programs to access the file while your program is operating on it.
#
# We are going to leave the workspace open for now, and remember to close it at the end.

# ## Objects and data
#
# When connecting to an existing `geoh5` file, the API will travel through the
# `Workspace` and collect minimal information about the `groups`, `objects` and
# `data` present on file. At the base of this parent/child hierarchy is the `Root` group.
# Every entity has a parent, except for the `root`. Note that no values are loaded unless directly requested.

# + tags=["clear-form"]
workspace.root.children
# -

# The `Workspace` itself has a few utility methods to quickly access all groups, objects or data registered.

# + tags=["clear-form"]
workspace.groups, workspace.objects, workspace.data
# -

# The `get_entity` method allows to retrieve entities by `name` or `uid`.

# + tags=["clear-form"]
grid = workspace.get_entity("SunCity")[0]
# -

# The `get_entity` always returns a `list`, as many entities could have the same name.

# + tags=["clear-form"]
f"I have recovered a {type(grid)} with uuid: {grid.uid}"
# -

# It is best-practice to instead use `get_entity` with a unique identifier (`uuid`)
# to guarantee access to a specific entity

# + tags=["clear-form"]
workspace.get_entity(grid.uid)[0] == grid
# -

# Likewise, data associated with an object can be accessed through the `children` attribute.
# To access data with values, the workspace must be re-opened if closed.

# + tags=["clear-form"]
grid.children
# -

# or with the utility method `get_data` to access it by name

# + tags=["clear-form"]
dem = grid.get_data("Band 1")[0]
# -

# Data values are accessed through the `values` attribute of the `data` entity.
# Let's use a third party plotting package `matplotlib` to display the information on file.

# + tags=["clear-form"]
plt.pcolormesh(
    grid.origin["x"] + grid.cell_center_u,
    grid.origin["y"] + grid.cell_center_v,
    dem.values.reshape(grid.shape),
)
# -

# ## Creating objects
#
# The `geoh5` format supports a wide range of object types as [documented here](https://geoh5py.readthedocs.io/en/stable/content/geoh5_format/analyst/objects.html#analyst-objects). For this training, we will create a simple `Points` object using the `.create()` method.
#

# For the `Points` to be fully defined, we need to at least assign vertices as an array of 3D coordinates `shape(*, 3)`.
# Let's add one point at the Sun City resort.

# + tags=["clear-form"]
point = Points.create(workspace, vertices=np.c_[510000, 7196500, 1150], name="Points")
# -

# For more examples on how to create other object types, visit the
# [geoh5py-Tutorial](https://geoh5py.readthedocs.io/en/stable/content/user_guide/core_entities.html#Entities)

# ## Adding data
#
# Similarly, we can add data to the Points to show the strength and direction of
# the dipole moment. We are going to group those data so that we can display them as arrow in ANALYST.

# + tags=["clear-form"]
params = point.add_data(
    {
        "moment": {"values": np.r_[1.0]},
        "inclination": {"values": np.r_[-62.11]},
        "declination": {"values": np.r_[-17.9]},
    }
)
prop_group = point.find_or_create_property_group(
    name="dipole", property_group_type="Dip direction & dip"
)
point.add_data_to_group(params[1:], prop_group)
# -

# Et voila!

workspace.close()

# Since we have closed workspace, you can now safely open the `suncity.geoh5` with ANALYST to see the result.
#
# ![grid2d](./images/grid2d.png)

#  Copyright (c) 2022 Mira Geoscience Ltd.
