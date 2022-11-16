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

# # Custom User Interface (ui.json)
#
#
# This section provides training on how to create custom user interface within Geoscience ANALYST using the [ui.json
# standard](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/index.html). In this section we are going to demonstrate how to:
#
# - [Create a basic user-interface programmatically](Create-a-ui.json)
# - Read and write a ui.json from file
# - Demonstrate how to set up ANALYST to run a custom program

# ## Creating a ui.json
#
# The `ui.json` format is based on the [json](https://www.json.org/json-en.html) standard - a format widely used in programming. Python comes by default with a [json](https://docs.python.org/3/library/json.html) module to read and write to file. All we need is a way to create the structure that ANALYST understands. We can make use of the [geoh5py.ui_json](https://geoh5py.readthedocs.io/en/stable/content/api/geoh5py.ui_json.html) module to get started.

from geoh5py.ui_json import InputFile, constants, templates

# First, we need the base components must contain a few base parameters, such as a `title` and a `run_command`. A `constants.default_ui_json` is available to quickly get starget:

my_ui = constants.default_ui_json.copy()
my_ui["title"] = "Hello World!"
my_ui

# Note that the `run_command` is currently set to `None`, and therefore nothing will be executed by ANALYST. We will get to that part later.
#
# You could write this dictionary directly to file using the built-in `json` module with
#
# ```
# import json
# with open("./assets/myUI.ui.json", "w", encoding="utf-8") as file:
#     json.dump(my_ui, file, indent=4)
# ```

# which writes it out as text file under the `assets` directory. From here you can drag & drop the file to the `Viewport` of ANALYST, which would render as:
#
# ![base_ui](./images/base_ui.png)
#
# This user-interface doesn't do much at the moment so we can add a few additional forms.
# More parameters can be added by a simple `update` of the base dictionary. You can use any of the 8 `forms` currently supported:
#
# ### [Bool value](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#boolean-parameter)
#
# Checkbox to set an option as true or false.
# ```
# my_ui.update({
#     "value_bool": templates.bool_parameter(label="True/false")
# })
# ```
#
# ![bool_ui](./images/bool_ui.png)
#
# ### [Integer value](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#integer-parameter)
#
# Value field for integers. It is possible to set min/max values to bound the output.
# ```
# my_ui.update({
#     "value_int": templates.integer_parameter(label="Some value:")
# })
# ```
#
# ![int_ui](./images/int_ui.png)
#
#
# ### [Float value](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#float-parameter)
#
# Value field for floats. Bounds on value also available.
# ```
# my_ui.update({
#     "value_float": templates.float_parameter(label="Some value:")
# })
# ```
#
# ![float_ui](./images/float_ui.png)
#
# ### [String value](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#string-parameter)
#
# String field for text value.
# ```
# my_ui.update({
#     "value_string": templates.string_parameter(label="Some value:")
# })
# ```
#
# ![string_ui](./images/string_ui.png)
#
#
# ### [Multi-choice string](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#multi-choice-string-parameter)
#
# Dropdown list of string values to chose from.
# ```
# my_ui.update({
#     "choice": templates.choice_string_parameter(label="Select:")
# })
# ```
#
# ![choice_string_ui](./images/choice_string_ui.png)
#
#
# ### [File choice](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#file-parameter)
#
# Button to browse for a file on disk.
# ```
# my_ui.update({
#     "file": templates.file_parameter(label="Select file:", fileType=["geoh5"], fileDescription=["project"])
# })
# ```
#
# ![file_ui](./images/file_ui.png)
#
#
# ### [Geoh5 Object selection](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#geoscience-analyst-object-parameter)
#
# Dropdown selection for objects listed under an active ANALYST session. The `mesh_type` attribute lets filter specific object types by their [uuid types](https://geoh5py.readthedocs.io/en/stable/content/geoh5_format/analyst/objects.html)
# ```
# my_ui.update({
#     "object": templates.object_parameter(label="Object", mesh_type="")
# })
# ```
#
# ![object_ui](./images/object_ui.png)
#
#
# ### [Geoh5 Data selection](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/json_objects.html#geoscience-analyst-data-parameter)
#
# Dropdown selection of data listed under the `parent` object.
# ```
# my_ui.update({
#     "object": templates.object_parameter(label="Object", mesh_type=""),
#     "data": templates.data_parameter(label="Data", parent="object")
# })
# ```
#
# ![data_ui](./images/data_ui.png)
#
# You are invited to click on the link provided for each form to read about the different options available to further control your UI.
#
# Once you are done adding forms:
#
# - Write this file out to disk
# - Drag & drop the ui.json to the viewport of ANALYST
# - Do some selections
# - Click `Apply` or `Ok` to write back out the ui.json.
#
# ![run_ui](./images/run_ui.png)

# ## Read from file
#
# The next step is to read the UI you have created to file, so that ANALYST can interpret it. We are going to take advantage of the [geoh5py.ui_json.InputFile](https://geoh5py.readthedocs.io/en/stable/content/api/geoh5py.ui_json.html#geoh5py.ui_json.input_file.InputFile) class to handle some of the value conversion between geoh5 and python.
#

ifile = InputFile.read_ui_json("../assets/myUI.ui.json")

# ## Example: Magnetic Dipole App
#
# In the previous section covering the [geoh5 API](geoh5-API), we have introduced functionality to compute the magnetic field from dipole locations. We are now going to create a user-interface (UI) to be able to run this program from a Geoscience ANALYST session.

#  Copyright (c) 2022 Mira Geoscience Ltd.

# # Custom User Interface (ui.json)
#
#
# This section provides training on how to create custom user interface within Geoscience ANALYST using the [ui.json
# standard](https://geoh5py.readthedocs.io/en/stable/content/uijson_format/index.html).

# ## UI.json format

# # Example 1: Electric field calculator (revisited)

#  Copyright (c) 2022 Mira Geoscience Ltd.
