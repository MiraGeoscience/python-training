# ---
# jupyter:
#   jupytext:
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

# # Classes
#
# While `functions` are common to almost all types programming languages, the concept of `Class` is specific to
# object-oriented languages. Objects are containers of methods (functions) and properties that can help better
# organize your code.
#
# We will demonstrate this idea by re-visiting the assay analysis done in the previous [Functions](Functions)
# section. We have two lists for `grades` and `depths`, and we want to create some mechanism to get the depths where
# values exceed some detection threshold.


# + tags=["clear-form"]
grades = [0.1, 0.02, 1.3, 2.4, 3.5, 0.01]
depths = [10, 55, 80, 105, 115, 120]
# -

# Let's first create a simple `Assay` class and copy over the functions `anomalous` and `get_depths`.


# + tags=["clear-form"]
class Assay:
    """Simple Assay class."""

    def __init__(self, arg_1: list, arg_2: list, threshold: float = 1.0):
        self.grades = arg_1
        self.depths = arg_2
        self.threshold = threshold

    def anomalous(self):
        """
        Find the elements of a list above threshold
        """
        return [val > self.threshold for val in self.grades]

    def get_depths(self):
        """
        Extract interval of values from bool logic
        """
        output = []
        for val, cond in zip(self.depths, self.anomalous()):
            if cond:
                output.append(val)
        return output

    def __call__(self):
        return self.get_depths()


# -

# We have defined an `Assay` class that contains both our previous functions that are now methods of the class.
#
# While it may not seem like we did much progress compared to the [Functions](Functions) implementation, we actually
# started creating structure that could be greatly beneficial down the road. Imagine that we had many assays coming
# from different drillholes, all with different lengths. Storing and computing the information through lists could
# rapidly become cumbersome, while dealing with a list of classes gives us a low-level organization of the data.

# We can now brake apart the components of class.
#
#
# ## `__init__` (Initialization)
#
#
# The `__init__` method lets us define things to do when the class is first `initialized`. Here we are expecting the
# user to input values for `grades` and `depths`, and left the `threshold` parameter as optional with a default of
# 1.0. Again we used `typing` with `:` to let know the user what kind of input they are. We then assigned those
# inputs to equivalent `attributes` of the class using the `self`.
#
# Initializing the class is done with

# + tags=["clear-form"]
assay = Assay(grades, depths)
type(assay)
# -

# ## self
#
# The `self` is a reserved Python keyword used within a classes to reference to itself. It is used to assign
# attributes on the class and access them back within the various methods. Note that our two methods `anomalous` and
# `get_depth` only take in `self` as input as the `grades`, `depths` and `threshold` can be accessed from the class.

# + tags=["clear-form"]
assay.grades
# -

# and likewise for methods

# + tags=["clear-form"]
assay.anomalous()
# -

# ## __call__
#
# The `__call__` method is an optional method specific to the action of calling the class. In this case we are simply
# going to perform the `self.get_depth()` method and return the result.

# + tags=["clear-form"]
assay()
# -

# ## @property
#
# It is sometimes preferable to add extra controls on the attributes of a class. For example if we would like to
# protect or validate the `threshold` parameter, we can explicitly create a `property` of the class with a `setter`
# method.


# + tags=["clear-form"]
class Assay2:
    """Simple Assay class."""

    def __init__(self, arg_1: list, arg_2: list, threshold: float = 1.0):
        self.grades = arg_1
        self.depths = arg_2
        self._threshold = threshold

    def anomalous(self):
        """
        Find the elements of a list above threshold
        """
        return [val > self.threshold for val in self.grades]

    def get_depths(self):
        """
        Extract interval of values from bool logic
        """
        output = []
        for val, cond in zip(self.depths, self.anomalous()):
            if cond:
                output.append(val)
        return output

    @property
    def threshold(self) -> float:
        """Cutoff value for anomalous assays."""

        return self.threshold

    @threshold.setter
    def threshold(self, value):
        if not isinstance(value, float):
            raise ValueError("The value for threshold must be a float.")

        self._threshold = value

    def __call__(self):
        return self.get_depths()


# -

# **A few highlights of the changes made to our `Assay` class.**
#
# - We are now using a `private` attribute `_threshold` to store the value, and use `threshold` as a property.
# Private attribute are meant to only be used within the class and not from the outside (private property - keep out!).
#
# - The `@property` allows to further document the attribute and indicate the return type using `-> float`.
#
# - The `@threshold.setter` lets us add validations on the value provided by a user. It is good coding practice to
# add checks on type to prevent a program to error later.
#
# - Here we used the built-in method `isinstance()` to check if the value is a `float`, and return a custom error
# message if it is not.

# + tags=["clear-form"]
assay = Assay2(grades, depths)
assay.threshold = 2.0
# -

#  Copyright (c) 2022 Mira Geoscience Ltd.
