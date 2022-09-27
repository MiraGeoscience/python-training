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

# # Python Fundamentals
#
# This section offers a brief overview and examples of core Python concepts and syntax. It is not meant to be a
# fully comprehensive resource for Python, but mainly a primer to get participants started with writing their first
# utility program.
#
# This training material uses the [jupyter-notebook](https://jupyter.org/) environment that contains blocks of text (
# like this one) and code running from a web browser environment (no internet required). Participants are invited to
# write and run the examples provided to get comfortable with the Python synthax. Here are few useful shortcuts for
# jupyter-notebooks.
#
#  - Press **esc + a** to add a cell above, or **esc+b** to add a cell below.
#  - Press **shift + enter** to run a selected cell.
#  - Click on a cell and press **M** to convert to a text cell, or **Y** to convert to code cell.
#
#
# ## Objects
#
# At the core, Python is an **object-oriented programming** (OOP) language that is defined by objects, also referred
# to as `Class`, that hold methods and attributes. Python programs are made of many of those objects that interact
# with each other to yield the desired output. This is in contrast to **imperative** or **procedural-based**
# languages, such as C and Fortran, that make use of functions and variables to create a series of computational
# steps executed in sequence. Python can also be written in a procedural way but internally objects are always doing
# the work.
#
# While often slower than imperative compiled languages, object-orientated programming languages like Python allow
# for more concise and readable code that is easy to share and repurposed. This will become obvious as we go further
# in this tutorial.
#
# Let's start by introducing some core Python objects.

# ### Numerics
#
# Numerical values can be of type `float` with decimals or of type `int` (integers). Floats are mainly used for
# arithmetic while integers are used to count or index arrays.
#
# ```
# # Integer
# x = 1
# print(type(x))
# ```
#
# ```
# # Float
# y = 1.0
# print(type(y))
# ```

# + tags=["hide-input"]
x = 1
print(type(x))

y = 1.0
print(type(y))
# -

# Note that we have used two important built-in methods: `print` and `type`. First, the `type` method returns the
# type of object given as input, then the `print` displays the result to screen. Input values for methods are always
# given between parentheses `()`.
#
# Here is a shortlist of standard arithmetic and logical operators in order of priority (evaluated in order).
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
#

# + tags=["hide-input"]
print(2**2 * 1.5 + 1 == 7.0)
# -

# Also, it is important to keep in mind general rules of return types.
#
# - Adding or subtracting integers yields an integer
#
#     ```
#     print(type(x+x))
#     ```
#
# - Multiplying or dividing integers yields a float
#     ```
#     print(type(x/x))
#     ```
#
# - Mix operations on integer and float always yield a float
#     ```
#     print(type(x+y))
#     ```

# + tags=["remove-cell"]
print(type(x + x))
print(type(x / x))  # Multiply|divide integers yields a float
print(type(x + y))  # Mix of integer and float yields a float
# -

# As previously mentioned, even if `x` is simply an integer, it is technically still a Python object with methods. To
# access the list of methods available, you can simply type `.` then the `tab` key.
#
# ![methods](./images/methods.png)

# In this case, the `imag` method of the integer would return the imaginary part of x (if it was a complex number).

# ### String
#
# Strings are text objects that contain characters (letters, numbers or symbols) isolated by single `'` or double
# `"` quotes. Both are acceptable but consistency is preferable.
#
# Here is a shortlist of useful methods that will be used in this tutorial.
#
# - Adding strings
#     ```
#     "hello" + " world"
#     ```
# - Upper/lower and single word capitalization
#     ```
#     "I" + " love ".upper() + "python".capitalize()
#     ```
# - Upper case every word
#     ```
#     "this is important".title()
#     ```
# - Find sub-string within
#     ```
#     "Long sentence with symbols #$%^&".find("sym")
#     ```

# + tags=["remove-cell"]
# Additions
print("hello" + " world")

# Title
print("this is important".title())

# Upper/lower and single word capitalization
print("I" + " love ".upper() + "python".capitalize())

# Title
print("this is important".title())

# Find
print("Long sentence with symbols #$%^&".find("sym"))
# -

# ### List
#
# List are simple containers for other objects, which can be of any type. They are created with square brackets `[]`.

a_list = [1.0, 2, "abc"]

# Here are a few important methods that can used on a `list`.

# Indexing (count starts at 0)
print(a_list[0])

# Removing an element
a_list.pop(0)
print(a_list)

# Elements within the list can be searched with the `index` method.
#
# ```
# a_list.index("abc")
# ```

# + tags=["remove-cell"]
a_list.index("abc")
# -

# ### Dictionary
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

# + tags=["remove-cell"]
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

# + tags=["remove-cell"]
print(my_dict["integer"])


# -

# ### Functions
#
# The general concept of programming is to define a set of operations for a computer to execute rapidly. The building
# blocks making up a program can be written in terms of a `function` that take in input values and return a result.
#
# Below are two trivial functions to `add` and `multiply` input values.

# +
def add(arg_a, arg_b):
    """Function to add elements"""
    return arg_a + arg_b


def multiply(arg_a, arg_b):
    """Function to multiply elements"""
    return arg_a * arg_b


# -

print(add(1, 2), multiply(1, 2))


# The two functions that take input `arguments` **a** and **b**, and return a value using built-in Python operators
# `+` and `*`. There are clear issues with the example above in terms coding standards, but it provides a base
# example for Python functions.
#
# See the [Best Practice](best_practice) page for additional material on style guides.

# #### Keyword Arguments
# Other than required input arguments, Python also allows for default values to be stored in
# the signature of the function as keyword arguments (`kwargs`). Let's suppose we would like to add optional constant
# multipliers to our function scale the result. We could re-write the `add` function as:


def add_kwargs(arg_a, arg_b, arg_c=1, arg_d=1):
    """Function to add elements scaled by constants."""
    return arg_c * arg_a + arg_d * arg_b


# such that `c` and `d` are optional inputs. If value are not provided then the defaults are used.

print(add_kwargs(1, 2))

# In this case, since the defaults are 1s, then we get the same result as previously. Optionally, users can supply
# new values to the keyword arguments in any order.

print(add_kwargs(1, 2, arg_d=2, arg_c=1))

# If not assigned specifically as keyword arguments, Python will simply distribute the extra arguments in the order
# defined in the signature of the function. For example

print(add_kwargs(1, 2, 1, 2) == add_kwargs(1, 2, arg_c=1, arg_d=2))


# Note that we have used the logical operator `==` to compare the output of two `add` calls.

# ### Classes
#
# While `functions` are common to almost all types programming languages, the concept of `Class` is specific to
# object-oriented languages. Objects are containers for methods (functions) and properties.  as shown with the
# following example.


class Arithmetic:
    """Simple class"""

    @staticmethod
    def add(var_a, var_b, var_c=1, var_d=1):

        """Method to add."""
        return var_c * var_a + var_d * var_b

    @staticmethod
    def multiply(var_a, var_b):
        """Method to add."""
        return var_a * var_b


# The class `arithmetic` can be seen as a container for mathematical operations, which contains an `add` and
# `multiply` method. Because those methods.
#
#
# Note: Within the jupyter-notebook environment, it is possible to query information about an attribute of class with
# the `?` symbol place immediately after
#
# ```
# arithmetic?
# ```

# # ## Importing packages
# #
# # The base objects described previously can be assembled together to do more complex operations. Python is made up
#
# import numpy as np
#
# # Here we have imported the entire package `numpy` and assign a short-hand alias for it to keep our code more
# # concise. Sub-modules can be accessed using a `.` such that
#
# print(np.array)
#
# # returns a function handle for the `array` class.
