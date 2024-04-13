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

# # Python Fundamentals
#
# Almost all computer programs can be broken down into simple operations that
# are stringed together to perform complex tasks. In this section, we introduce
# core Python concepts and syntax that would be required to write Python programs.

# ## Variables
#
# A key component of programming is the storage of information in a computer
# memory as **variables**. It is a way to assign small blocks of data with a label
# that is human-readable. We will start with simple **numerical** and **string** variables.
#
# ## Numerics
#
# Numerical values can be of type `float` with decimals or of type `int` (integers). Floats are mainly used for
# arithmetic while integers are commonly used to count or index arrays.

# + tags=["clear-form"]
x = 1
type(x)
# -

# We have created our first numerical variable **x** for which the computer as a pointer to the `int` value of **1**.
# Note that we have also used two built-in Python methods: `print` and `type`.
#
# - The `type` **method** gets evaluated and returns the type of the **object**
#   (see [notes below](Quick-note-on-Objects)). Input values for methods are always
#   given between parentheses `()`.
# - The `print` method displays the result to screen.
#
# Now let's create a second variable **y** of numerical type `float`

# + tags=["clear-form"]
y = 1.0
type(y)
# -

# ## Operations
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
# For example:

# + tags=["clear-form"]
2**2 * 1.5 + 1 == 7.0
# -

# You can verify the result above by doing the operations in your head. It is important to keep in mind general rules
# of return types for numerical values.
#
# - Adding or subtracting integers yields an integer

# + tags=["clear-form"]
type(x + x)
# -

# - Multiplying or dividing integers yields a float

# + tags=["clear-form"]
type(x / x)
# -

# - Mix operations on integer and float always yield a float

# + tags=["clear-form"]
type(x + y)
# -

# ## Strings
#
# Strings are text objects that contain characters (letters, numbers or symbols) isolated by single `''` or double
# `""` quotes. Both are acceptable but consistency throughout your code is preferable.
#
# Here is a shortlist of useful methods that can be used on strings.
#
# - Adding

# + tags=["clear-form"]
"hello" + " world"
# -

# - Upper/lower and single word capitalization

# + tags=["clear-form"]
"I" + " love ".upper() + "python".capitalize()
# -

# - Upper case every word

# + tags=["clear-form"]
"this is important".title()
# -

# - Find sub-string within

# + tags=["clear-form"]
"Long sentence with symbols #$%^&".find("sym")
# -

# ## Objects
#
# At the core, Python is an **object-oriented** programming (OOP) language.
# In short, a computer program is made up of many object variables that hold
# **attributes** and **methods** specific to itself. An **object** is also
# referred to as a `Class`. Think of it as a small machine that takes inputs,
# store values and does operations on request. Objects can interact with each other
# to form a program. Object-oriented programming allows for concise code that is
# easy to read and share with others - which explains the popularity of Python in the world of open-source.
#
# ![oop](./images/object_oriented.png)
#
# This is somewhat in contrast to **imperative** or **procedural-based** languages, such as **C** and **Fortran**. In an
# imperative framework, variables and functions are chained to form a series of computational steps executed in
# sequence, but variables themselves don't do anything - they are simple container of data.
#
# ![imperative](./images/imperative.png)
#
# Python can also be written in a procedural way, but internally objects are always doing the work.
#
# Take for example the numeric variables `x` introduced previously.
# While it appears to be a simple integer, it is still a Python object with methods.
# You can access the list of methods available to that specific object by typing `.`
# then the `tab` key after the variable
#
# ![methods](./images/methods.png)
#
# In this case, the `imag` method of the integer would return the imaginary part
# of x (if it was a complex number). In a future section on [Classes](classes),
# you will be able to create your own type of object with custom methods.
# To be continued.
#

#  Copyright (c) 2022 Mira Geoscience Ltd.
