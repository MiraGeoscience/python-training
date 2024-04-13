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

# # Importing Packages
#
# Python has over 200,000 registered packages, and so a big part of becoming proficient has to do with importing
# third-party libraries.
#
# ```
# import numpy as np
# ```

import numpy as np

# Here we have imported the entire package [numpy](https://numpy.org/) and assign a short-hand alias for it to keep
# our code more concise. Sub-modules can be accessed using a `.` such that

print(np.array)

# returns a function handle for the `array` class.

#  Copyright (c) 2022 Mira Geoscience Ltd.
