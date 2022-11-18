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
# The general concept of programming is to define a set of operations for a computer to execute. The building blocks
# making up a program can be written in terms of a `function` that take in input values and return a result. In its
# simplest form, a function (or method) is defined with:


# + tags=["clear-form"]
def fun(arg):
    """
    Some function.

    :param arg: Some input argument.
    """
    return arg


# -

# Let's brake this down.
#
# -  The `def` keyword marks the beginning of the function signature. Everything that is part of a function must be
# indented (1 tab or 4 spaces) below it.
#
# - Input arguments (`arg`) are added within the parenthesis. The signature ends with a column `:`.
#
# - It is good practice adding `docstrings` to document what the function does and what the input parameters are. The
# block of text is bookended by triple quotes (`"""`).
#
# See the [Best Practice](best_practice) section for additional styling guides.

# In this case, the `fun` function simply takes an input argument `arg` and returns it back.

# + tags=["clear-form"]
print(fun("abc"))
# -

# ## For loop
#
# We will try again with a slightly more interesting example that uses a `for` loop iterator. Say we are given assay
# results down a drillhole.

# + tags=["clear-form"]
grades = [0.1, 0.02, 1.3, 2.4, 3.5, 0.01]
depths = [10, 55, 80, 105, 115, 120]
# -

# We would like to know the `depths` where `grades` are above 1.
#
# There are many (faster) to solve this problem, but let's first find the grade values above some threshold.


# + tags=["clear-form"]
def anomalous(values, threshold):
    """
    Find the elements of a list above threshold
    """
    bool_list = []
    for val in values:
        bool_list.append(val > threshold)

    return bool_list


# -

# The `anomalous` function takes in as input a list of grade `values` and a `threshold`,
# then returns a list of `bool`'s (true or false) to indicate which elements are above 1.
# This function performs three steps
#   - Use a `for` loop iterator to visit every element of the list.
#   - Check if the element is above threshold with logic ">".
#   - Add the result to a `logic` list using the `.append` method.

# Calling this method on our `grades` with a `threshold`= 1.0 yields

# + tags=["clear-form"]
logic = anomalous(grades, 1.0)
logic
# -

# Note that the same operation could also have been done with an `in-line` approach such that

# + tags=["clear-form"]
logic = [val > 1.0 for val in grades]
logic
# -

# In-line operations are more compact (and usually faster) than appending values within a `for` loop operation,
# and would have not required to create the `anomalous` function. In the end, both gives back the same result.

# ### Keyword Arguments
#
# Other than the required input arguments, Python also allows for default values to be stored
# in the signature of the function as keyword arguments (`kwargs`). Let's suppose we would like to set a default
# value for the `threshold`. We could re-write the `anomalous` function as:


# + tags=["clear-form"]
def anomalous(values, threshold=1.0):  # pylint: disable=E0102
    """
    Find the elements of a list above threshold
    """
    bool_list = []
    for val in values:
        bool_list.append(val > threshold)

    return bool_list


# -

# Since `threshold` already has a value, then the argument becomes optional and the function still runs without it.

# + tags=["clear-form"]
anomalous(grades)
# -

# If not assigned specifically as keyword arguments, Python will simply distribute the extra arguments in the order
# defined in the signature of the function. For example

# + tags=["clear-form"]
anomalous(grades, 2.0)
# -

# ## Example 2: If statement
#
# Next in our assay analysis, we would like get the depth interval for the anomalous grades. We can write a second
# function that takes the result of `anomalous` such that


# + tags=["clear-form"]
def get_depths(values: list, conditions: list[bool]):
    """
    Extract interval of values from bool logic
    """
    output = []
    for val, cond in zip(values, conditions):
        if cond:
            output.append(val)
    return output


# -

# The `get_depths` function takes in two lists, one of values and another one for the logic (`bool`), and returns a
# subset of values if the `conditions` are `True`. Here are a few Python details to highlight
#
# - The `if` statement used to test a condition (true or false). Other conditions are
#     - `elif`: Always follows and if statement, requires a condition.
#     - `else`: Always used at the end of `if` statements, no condition used.
# - The `zip` method allows iterating over multiple lists at the same time.
#   If the inputs have different lengths, the iteration will stop once it reaches the end of the shortest list.
#
# - We use `typing` (e.g. `conditions: list[bool]`) in the signature of the function to
#   specify the type required for the input arguments. The type is not enforced on runtime,
#   but mainly good-practice as it can be used for code analysis and documentation.


# Calling the `get_depths` method with the `grades` and `logic` previously computed we get

# + tags=["clear-form"]
get_depths(grades, logic)
# -

#  Copyright (c) 2022 Mira Geoscience Ltd.
