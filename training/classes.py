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


class Assay:
    """Simple Assay class."""

    def __init__(self, depths: list, values: list, threshold=1.0):
        self.depths = depths
        self.values = values
        self.threshold = threshold

    @staticmethod
    def anomalous(values, threshold=1.0):
        """
        Find the elements of a list above threshold
        """
        return [val > threshold for val in values]

    def get_depths(self):
        """
        Extract interval of values from anomalous values
        """
        conditions = self.anomalous(self.values, self.threshold)
        output = []
        for val, logic in zip(self.depths, conditions):
            if logic:
                output.append(val)
        return output

    def __call__(self):
        return self.get_depths()


# The class `Assay` can be seen as a container for mathematical operations, which contains an `anomalous` and
# `get_depths` method. Because those methods
#
#
# Note: Within the jupyter-notebook environment, it is possible to query information about an attribute of class with
# the `?` symbol place immediately after
#
# ```
# arithmetic?
# ```

#  Copyright (c) 2022 Mira Geoscience Ltd.
