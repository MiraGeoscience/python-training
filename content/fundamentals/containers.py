# ---
# jupyter:
#   jupytext:
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

# # Containers
#
# In the previous section, we have introduced numerics of type `int` and `float`, as well as text variable. Often we would like to group many of numerics or strings together to perform larger operations. This section introduces classes of containers to group values together.

# ## List
#
# Lists are generic containers for other objects, which can be of any type. They are created with square brackets `[]`.

# + tags=["clear-form"]
a_list = [1.0, 2, "abc"]
# -

# Here are a few important methods that can used on a `list`.
#
# - Indexing (accessing) elements of the list (count starts at 0)

# + tags=["clear-form"]
a_list[0]
# -

# - Adding (appending) to the list.

# + tags=["clear-form"]
a_list += ["new"]
a_list
# -

# - Removing an element from the list using the `pop` method with index

# + tags=["clear-form"]
a_list.pop(0)
a_list
# -

# - Finding the `index` of an element within the list. The same method applies to [string](String) objects.

# + tags=["clear-form"]
a_list.index("abc")
# -

# ## Dictionary
#
# Dictionaries (`dict`) are also containers for objects but give an additional level of structure over lists as every
# value of the dictionary is indexed by a `key`. A dictionary is created with a list of `key: value` pairs within
# braces `{}`.

# + tags=["clear-form"]
my_dict = {"integer": 2}
# -

# Here are a few important methods that can used on a `dict`.
#
# - Accessing values using the key

# + tags=["clear-form"]
my_dict["integer"]
# -

# - Adding entries

# + tags=["clear-form"]
my_dict["new"] = 123
my_dict
# -

# - Removing entries

# + tags=["clear-form"]
del my_dict["new"]
my_dict
# -

# - Looping over keys

# + tags=["clear-form"]
list(my_dict)
# -

# - Looping over values

# + tags=["clear-form"]
list(my_dict.values())
# -

# - Looping over both keys and values

# + tags=["clear-form"]
list(my_dict.items())
# -

#  Copyright (c) 2022 Mira Geoscience Ltd.
