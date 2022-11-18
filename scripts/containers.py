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

a_list = [1.0, 2, "abc"]

# Here are a few important methods that can used on a `list`.
#
# - Indexing (accessing) elements of the list (count starts at 0)
#     ```
#     a_list[0]
#     ```

# + tags=["remove-input"]
print(a_list[0])
# -

# - Adding (appending) to the list.
#     ```
#     a_list += ["new"]
#     print(a_list)
#     ```

# + tags=["remove-input"]
a_list += ["new"]
print(a_list)
# -

# - Removing an element from the list using the `pop` method with index
#     ```
#     a_list.pop(0)
#     print(a_list)
#     ```

# + tags=["remove-input"]
a_list.pop(0)
print(a_list)
# -

# - Finding the `index` of an element within the list. The same method applies to [string](String) objects.
#     ```
#     a_list.index("abc")
#     ```

# + tags=["remove-input"]
print(a_list.index("abc"))
# -

# ## Dictionary
#
# Dictionaries (`dict`) are also containers for objects but give an additional level of structure over lists as every
# value of the dictionary is indexed by a `key`. A dictionary is created with a list of `key: value` pairs within
# braces `{}`.
#
# ```
# my_dict = {
#     "float": 1.0,
#     "integer": 2,
#     "string": "abc",
# }
# ```

# + tags=["remove-input"]
my_dict = {"integer": 2}
# -

# Here are a few important methods that can used on a `dict`.
#
# - Accessing values using the key
#
#     ```
#     my_dict["function"]
#     ```

# + tags=["remove-input"]
print(my_dict["integer"])
# -

# - Adding entries
#     ```
#     my_dict["new"] = 123
#     ```

# + tags=["remove-input"]
my_dict["new"] = 123
print(my_dict)
# -

# - Removing entries
#     ```
#     del my_dict["new"]
#     ```

# + tags=["remove-input"]
del my_dict["new"]
print(my_dict)
# -

# - Looping over keys
#     ```
#     list(my_dict)
#     ```

# + tags=["remove-input"]
print(list(my_dict))
# -

# - Looping over values
#     ```
#     list(my_dict.values()]
#     ```

# + tags=["remove-input"]
print(list(my_dict.values()))
# -

# - Looping over both keys and values
#     ```
#     list(my_dict.items())
#     ```

# + tags=["remove-input"]
print(list(my_dict.items()))
# -

#  Copyright (c) 2022 Mira Geoscience Ltd.
