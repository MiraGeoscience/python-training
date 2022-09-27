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

# # Functions
#
# The general concept of programming is to define a set of operations for a computer to execute. The building
# blocks making up a program can be written in terms of a `function` that take in input values and return a result. In its simplest form, a function (or method) is defined with the `def` keyword:
#
# ```
# def fun(arg):
#     """A trivial function."""
#     return arg
# ```
#
# Everything that is part of a function must be indented (1 tab or 4 spaces) under the signature ending with `:`. It is also good practice to add `docstrings` with triple quotes (`"""`) to document what the function does.
#
# See the [Best Practice](best_practice) page for additional styling guides.

# In this case, the `fun` function simply takes an input argument `arg` and returns it back.
# ```
# fun("abc")
# ```

# + tags=["remove-input"]
def fun(arg):
    """Some function."""
    return arg


fun("abc")
# -

# ## Example 1: For loop
# Let's take a look at a sightly more interesting problem. Say we are given assay results down a drillhole.
#
# ```
# grades = [0.1, 0.02, 1.3, 2.4, 3.5, 0.01]
# depths = [10, 55, 80, 105, 115, 120]
# ```

# + tags=["remove-input"]
grades = [0.1, 0.02, 1.3, 2.4, 3.5, 0.01]
depths = [10, 55, 80, 105, 115, 120]


# -

# We would like to know the `depths` where `grades` are above 1.
#
# There are many ways to go about this, but as a start we are going to use a `for` loop within a function. First we need to find the grade values above some threshold
#
# ```
# def anomalous(values, threshold):
#     """
#     Find the elements of a list above threshold
#     """
#     logic = []
#     for val in values:
#         logic.append(val > threshold)
#
#     return logic
# ```
#
# The `anomalous` function takes in as input a list of grade `values` and a `threshold`, then returns a list of `bool`'s (true or false) to indicate which elements are above 1. This function performs three steps
#   - Use a `for` loop iterator to visit every element of the list.
#   - Check if the element is above threshold with logic ">".
#   - Add the result to a `logic` list using the `.append` method.

# + tags=["remove-input"]
def anomalous(values, threshold):
    """
    Find the elements of a list above threshold
    """
    logic = []
    for val in values:
        logic.append(val > threshold)

    return logic


# -

# Calling this method on our `grades` with a `threhsold`= 1.0 yields
# ```
# logic = anomalous(grades, 1.0)
# print(logic)
# ```

# + tags=["remove-input"]
logic = anomalous(grades, 1.0)
print(logic)
# -

# Note that the same operation could also have been done with an `in-line` approach such that
# ```
# logic = [val > threshold for val in grades]
# ```
# In-line operations are more compact (and usually faster) than appending values within a `for` loop operation, and would have not required to create the `anomalous` function. In the end, both gives back the same result.
# ```
# print(logic)
# ```

# + tags=["remove-input"]
logic = [val > 1.0 for val in grades]
print(logic)


# -

# ### Keyword Arguments
# Other than the required input arguments, Python also allows for default values to be stored in
# the signature of the function as keyword arguments (`kwargs`). Let's suppose we would like to set a default value for the `threshold`. We could re-write the `anomalous` function as:
#
# ```
# def anomalous(values, threshold=1.0):
#     """
#     Find the elements of a list above threshold
#     """
#     logic = []
#     for val in values:
#         logic.append(val > threshold)
#
#     return logic
# ```

# + tags=["remove-input"]
def anomalous(values, threshold=1.0):
    """
    Find the elements of a list above threshold
    """
    logic = []
    for val in values:
        logic.append(val > threshold)

    return logic


# -

# Since `threshold` already has a value, then the argument becomes optional and the function still runs without it.
# ```
# anomalous(grades)
# ```

# + tags=["remove-input"]
anomalous(grades)
# -

# If not assigned specifically as keyword arguments, Python will simply distribute the extra arguments in the order
# defined in the signature of the function. For example
#
# ```
# anomalous(grades, 2.0)
# ```

# + tags=["remove-input"]
anomalous(grades, 2.0)
# -

# ## Example 2: If statement
#
# Next in our assay analysis, we would like get the depth interval for the anomalous grades. We can write a second function that takes the result of `anomalous` such that
#
# ```
# def intervals(
# ```

#  Copyright (c) 2022 Mira Geoscience Ltd.
