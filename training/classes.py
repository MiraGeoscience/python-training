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

# # Classes
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

#  Copyright (c) 2022 Mira Geoscience Ltd.
