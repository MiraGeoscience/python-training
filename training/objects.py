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
# At the core, Python is an **object-oriented programming** (OOP) language that is defined by a `Class` structure. Each `class` holds methods and attributes specific to itself. You can think of a `Class` as a small machine that can inputs, store things and do operations or interact with other parts. Python programs are made of many of those objects that are connected to each other and cooperate to yield the desired output.
#
# This is somewhat in contrast to **imperative** or **procedural-based** languages, such as C and Fortran. In an imperative framwork, variables and functions are generated and passed down to a series of computational steps executed in sequence. While often slower than imperative compiled languages, OOP languages like Python allow for more concise code that is easier to read and share. Python can also be written in a procedural way, but internally objects are always doing the work. This will become obvious as we go further in this tutorial.
#
# Let's start by introducing some core Python objects.

# ## Numerics
#
# Numerical values can be of type `float` with decimals or of type `int` (integers). Floats are mainly used for
# arithmetic while integers are used to count or index arrays.
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
# First, the `type` method is evaluated and it returned the type (`Class`) of the object given as input.
# Secondly, the `print` method displays the result to screen. Input values for methods are always given between parentheses `()`.

# As previously mentioned, even if `x` is simply an integer, it is technically still a Python object with methods. To
# access the list of methods available, you can simply type `.` then the `tab` key.
#
# ![methods](./images/methods.png)
#
# In this case, the `imag` method of the integer would return the imaginary part of x (if it was a complex number).

# ### Mathematical operations
#
# Here is a shortlist of standard arithmetic and logical operators that can be applied on numerical values (in order of priority of operation).
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
2**2 * 1.5 + 1 == 7.0
# -

# You can verify the result above by doing the operations in your head. It is important to keep in mind general rules of return types for numerical values.
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
# Strings are text objects that contain characters (letters, numbers or symbols) isolated by single `'` or double
# `"` quotes. Both are acceptable but consistency throughout your code is preferable.
#
# Here is a shortlist of useful methods that will be used in this tutorial.
#
# - Adding strings
#     ```
#     "hello" + " world"
#     ```

# + tags=["remove-input"]
# Additions
"hello" + " world"
# -

# - Upper/lower and single word capitalization
#     ```
#     "I" + " love ".upper() + "python".capitalize()
#     ```

# + tags=["remove-input"]
# Upper/lower and single word capitalization
"I" + " love ".upper() + "python".capitalize()
# -

# - Upper case every word
#     ```
#     "this is important".title()
#     ```

# + tags=["remove-input"]
# Title
"this is important".title()
# -

# - Find sub-string within
#     ```
#     "Long sentence with symbols #$%^&".find("sym")
#     ```

# + tags=["remove-input"]
# Find
"Long sentence with symbols #$%^&".find("sym")
# -

# ## List
#
# List are generic containers for other objects, which can be of any type. They are created with square brackets `[]`.

# + tags=["remove-input"]
a_list = [1.0, 2, "abc"]
# -

# Here are a few important methods that can used on a `list`.
#
# - Indexing (accessing) elements of the list (count starts at 0)
#     ```
#     a_list[0]
#     ```

# + tags=["remove-input"]
a_list[0]
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

# - Removing an element from the list using the index
#     ```
#     a_list.pop(0)
#     print(a_list)
#     ```

# + tags=["remove-input"]
a_list.pop(0)
print(a_list)
# -

# - Finding the index of an element within the list. The same method applies to [string](String) objects.
#     ```
#     a_list.index("abc")
#     ```

# + tags=["remove-input"]
a_list.index("abc")
# -

# ## Dictionary
#
# Dictionaries are also containers for objects but give an additional level of structure over lists. Every entry of
# the dictionary is indexed by a `key`. They are created with braces `{}` with `{key: value}` pairs separated by a
# column `:`.
#
# ```
# my_dict = {
#     "float": 1.0,
#     "integer": 2,
#     "string": "abc",
#     "function": add,
#     "class": arithmetic
# }
# ```

# + tags=["remove-input"]
my_dict = {
    "float": 1.0,
    "integer": 2,
    "string": "abc",
}
# -

# Values of the dictionary can then be accessed using the key
#
# ```
# my_dict["function"]
# ```

# + tags=["remove-input"]
my_dict["integer"]
# -

#  Copyright (c) 2022 Mira Geoscience Ltd.
