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

# # Objects
#
# At the core, Python is an **object-oriented programming** (OOP) language that is defined by a `Class` structure.
# Each `class` holds methods and attributes specific to itself. You can think of a `Class` as a small machine that
# takes inputs, stores properties and does operations. Classes can interact with each other to form a program.
# Object-oriented programming allows for concise code that is easy to read and share with others - which explains the
# popularity of Python in the world of open-source.
#
# ![oop](./images/object_oriented.png)
#
# This is somewhat in contrast to **imperative** or **procedural-based** languages, such as C and Fortran. In an
# imperative framework, variables and functions are chained to form a series of computational steps executed in
# sequence.
#
#
# ![imperative](./images/imperative.png)
#
# Python can also be written in a procedural way, but internally objects are always doing the work. This will become
# obvious as we go further in this tutorial.
#
# Let's start by introducing some core Python objects.

# ## Numerics
#
# Numerical values can be of type `float` with decimals or of type `int` (integers). Floats are mainly used for
# arithmetic while integers are commonly used to count or index arrays.
#
# ```
# # Integer
# x = 1
# print(type(x))
# ```

# + tags=["remove-input"]
x = 1
print(type(x))
# -

# ```
# # Float
# y = 1.0
# print(type(y))
# ```

# + tags=["remove-input"]
y = 1.0
print(type(y))
# -

# Note that we have used two built-in methods: `print` and `type`.
#
# First, the `type` method gets evaluated and returns the type (`Class`) of the object given as input.
#
# Secondly, the `print` method displays the result to screen. Input values for methods are always given between
# parentheses `()`.

# As previously mentioned, even if `x` is simply an integer, it is technically still a Python object with methods. To
# access the list of methods available, you can simply type `.` then the `tab` key.
#
# ![methods](./images/methods.png)
#
# In this case, the `imag` method of the integer would return the imaginary part of x (if it was a complex number).

# ### Mathematical operations
#
# Here is a shortlist of standard arithmetic and logical operators that can be applied on numerical values (in order
# of priority of operation).
#
# - `**`: Power
# - `%` : Modulo
# - `*`: Multiplication
# - `\`: Division
# - `+`: Addition
# - `-`: Subtraction
# - `==`: Logical equal
# - `>` : Logical greater than
# - `<` : Logical smaller than
#
# For example
#
# ```
# 2**2 * 1.5 + 1 == 7.0
# ```

# + tags=["remove-input"]
print(2**2 * 1.5 + 1 == 7.0)
# -

# You can verify the result above by doing the operations in your head. It is important to keep in mind general rules
# of return types for numerical values.
#
# - Adding or subtracting integers yields an integer
#
#     ```
#     type(x+x)
#     ```

# + tags=["remove-input"]
type(x + x)
# -

# - Multiplying or dividing integers yields a float
#     ```
#     type(x/x)
#     ```

# + tags=["remove-input"]
type(x / x)  # Multiply|divide integers yields a float
# -

# - Mix operations on integer and float always yield a float
#     ```
#     type(x+y)
#     ```

# + tags=["remove-input"]
type(x + y)  # Mix of integer and float yields a float
# -

# ## String
#
# Strings are text objects that contain characters (letters, numbers or symbols) isolated by single `''` or double
# `""` quotes. Both are acceptable but consistency throughout your code is preferable.
#
# Here is a shortlist of useful methods that can be used on strings.
#
# - Adding
#     ```
#     "hello" + " world"
#     ```

# + tags=["remove-input"]
# Additions
print("hello" + " world")
# -

# - Upper/lower and single word capitalization
#     ```
#     "I" + " love ".upper() + "python".capitalize()
#     ```

# + tags=["remove-input"]
# Upper/lower and single word capitalization
print("I" + " love ".upper() + "python".capitalize())
# -

# - Upper case every word
#     ```
#     "this is important".title()
#     ```

# + tags=["remove-input"]
# Title
print("this is important".title())
# -

# - Find sub-string within
#     ```
#     "Long sentence with symbols #$%^&".find("sym")
#     ```

# + tags=["remove-input"]
# Find
print("Long sentence with symbols #$%^&".find("sym"))
# -

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
