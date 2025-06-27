#!/usr/bin/env python

# (Functions)=
# # Functions
#
# In programming, we often need to perform the same set of operations multiple times. Instead of repeating the same code, we can create a **function** - a reusable block of code that performs a specific task.
#
# Functions are essential building blocks in Python that allow us to:
# - Organize code into logical, reusable pieces
# - Reduce code duplication
# - Make our programs easier to understand and maintain
#
# This section introduces how to create and use functions in Python.

# ## Creating a Simple Function
#
# In its simplest form, a function is defined using the `def` keyword followed by a name, parameters in parentheses, and a colon. The function body is indented below.
#

# In[13]:


def fun(arg):
    """
    A simple function that returns the input argument.

    :param arg: The input argument to return.
    :return: The same input argument.
    """
    return arg  # Return the input argument


# ## Function Anatomy
#
# Let's break down the structure of a function:
#
# ```
# def function_name(parameter1, parameter2):
#     """
#     Documentation string (docstring) explaining what the function does.
#
#     :param parameter1: Description of the first parameter.
#     :param parameter2: Description of the second parameter.
#     :return: Description of what the function returns.
#     """
#     # Function body - code that executes when the function is called
#     result = parameter1 + parameter2
#     return result  # Value to send back to whoever called the function
# ```
# - The `def` keyword marks the beginning of the function definition.
# - Everything that belongs to the function must be indented (4 spaces or 1 tab).
# - Parameters (like `parameter1` and `parameter2`) are inputs that the function can
#  use.
# - A **docstring** (triple-quoted string) explains what the function does and
# documents its parameters. It's best practice to include a docstring for every
#  function.
# - The `return` statement specifies what value the function sends back when it's
# done.

# In this case, the `fun` function simply takes an input argument `arg` and returns it back.

# In[14]:


print(fun("abc"))


# ## Functions with Multiple Parameters
# Functions can take multiple parameters separated by commas:

# In[15]:


def add(a, b):
    """
    Add two numbers together.

    :param a: First number.
    :param b: Second number.
    :return: The sum of a and b.
    """
    return a + b


# In[17]:


result = add(5, 7)
print(f"5 + 7 = {result}")


# ## For Loops
#
# Let's now look at a slightly more interesting example that uses a `for` loop
# iterator. Say we
#  are given assay
# results down a drillhole:

# In[18]:


grades = [0.1, 0.02, 1.3, 2.4, 3.5, 0.01]  # Concentration values
depths = [10, 55, 80, 105, 115, 120]  # Depths in meters


# Suppose we want to identify which samples have concentrations above a certain
#  threshold.
#
# Let's create a function that can identify these high-value samples:

# In[21]:


def find_high_grades(values, threshold):
    """
    Find the elements of a list that are above a specified threshold.

    :param values: List of numeric values to check
    :param threshold: The minimum value to be considered "high grade"
    :return: A list of True/False values indicating which elements exceed the threshold
    """
    result_list = []

    # Loop through each value in the list
    for value in values:
        # Check if this value is above our threshold
        is_high_grade = value > threshold

        # Add the result (True or False) to our list
        result_list.append(is_high_grade)

    return result_list


# Now let's use this function to find samples with grades above 1.0:

# In[28]:


# Find which samples have grades above 1.0
high_grade_indicators = find_high_grades(grades, 1.0)


# ## Default Parameter Values (Keyword Arguments)
#
# Python allows you to define default values for parameters in functions,
# making them optional when calling the function. These are called **keyword
# arguments** (kwargs). If you don't provide a value for a parameter with a default,
#  Python will use the default value instead:

# In[23]:


def find_high_grades(values, threshold=1.0):
    """
    Find the elements of a list that are above a specified threshold.

    :param values: List of numeric values to check
    :param threshold: The minimum value to be considered "high grade" (default: 1.0)
    :return: A list of True/False values indicating which elements exceed the threshold
    """
    result_list = []

    for value in values:
        is_high_grade = value > threshold
        result_list.append(is_high_grade)

    return result_list


# Now we can call the function without specifying the `threshold` parameter, and it will use the default value of 1.0:

# In[24]:


# Using the default threshold of 1.0
result_default = find_high_grades(grades)
print("Using default threshold (1.0):", result_default)

# Specifying a different threshold
result_custom = find_high_grades(grades, 2.0)
print("Using custom threshold (2.0):", result_custom)


# ## Conditional Logic with `if` Statements
#
# Now let's create a function that extracts the depths where our high-grade
# samples were found:

# In[26]:


def get_matching_values(values, conditions):
    """
    Extract elements from a list where the corresponding condition is True.

    :param values: List of values to filter
    :param conditions: List of True/False values (must be same length as values)
    :return: A list containing only the values where the condition was True
    """
    result = []

    # Loop through both values and conditions simultaneously
    for value, condition in zip(
        values, conditions
    ):  # `zip` pairs elements from both lists
        if condition:  # Check if the condition is True
            result.append(value)  # Add the value to the result if condition is True

    return result


# The `if` statement checks a condition and only executes the indented code
# below it if the condition is `True`.
#
# The `zip()` function is very useful - it allows us to iterate through
# multiple lists at the same time, pairing elements together.
#
# Now let's use this function to get the depths where our high-grade samples were found:

# In[31]:


# Get depths where grade is above 1.0
high_grade_depths = get_matching_values(depths, high_grade_indicators)
print("Depths with high-grade samples:", high_grade_depths)


# ## Function Type Hints
#
# Python allows you to add **type hints** to your functions. Type hints are not
#  enforced by Python, but they help document the expected types of parameters
#  and return values. This makes your code easier to understand and helps code
#  analysis tools catch potential errors:

# In[ ]:


def get_matching_values(values: list, conditions: list[bool]) -> list:
    """
    Extract elements from a list where the corresponding condition is True.

    :param values: List of values to filter
    :param conditions: List of True/False values (must be same length as values)
    :return: A list containing only the values where the condition was True
    """
    result = []

    for value, condition in zip(values, conditions):
        if condition:
            result.append(value)

    return result


# Type hints are especially helpful in larger projects where you want to make
# sure your functions are used correctly.

# ## Putting It All Together
# Now we can combine our functions to solve our original problem - finding the depths where there are high-grade samples:

# In[33]:


def find_high_grade_locations(
    grades: list, depths: list, threshold: float = 1.0
) -> list:
    """
    Find the depths where grades are above a threshold.


    :param grades: List of grade values
    :param depths: List of corresponding depths
    :param threshold: Minimum grade value of interest (default: 1.0)
    :return: List of depths where grades exceed the threshold
    """
    # First, identify which grades are high
    high_grade_indicators = [grade > threshold for grade in grades]

    # Then, get the corresponding depths
    high_grade_locations = []
    for depth, is_high in zip(depths, high_grade_indicators):
        if is_high:
            high_grade_locations.append(depth)

    return high_grade_locations


# In[34]:


# Find locations of grades above 2.0
result = find_high_grade_locations(grades, depths, 2.0)
print(f"High-grade locations (above 2.0): {result}")


# ## Summary: What You've Learned
# - **Functions** are reusable blocks of code that perform specific tasks
# - Functions are defined using the `def` keyword followed by a name and parameters
# - Functions can take **parameters** (inputs) and return values using the
# `return` statement
# - **Docstrings** document what a function does and how to use it
# - **Default parameter values** make parameters optional when calling a function
# - **For loops** allow you to iterate through items in a list
# - **If statements** let you include conditional logic in your functions
# - **Type hints** help document expected input and output types

# ## Knowledge Check: Python Functions
#
# ### 1. What keyword is used to define a function in Python?
# a) `function` \
# b) `def` \
# c) `func` \
# d) `define`
#
# ---
#
# ### 2. Which of the following correctly defines a function with a default parameter value?
# a) `def example(a, b = 10):` \
# b) `def example(a = int, b):` \
# c) `def example(a: default = 5, b):` \
# d) `def example(a: 5, b):`
#
# ---
#
# ### 3. What does the following function return when called with `result = multiply(4, 5)`?
# ```
# def multiply(x, y):
#     product = x * y
#     return product
# ```
#
# a) Nothing \
# b) `product` \
# c) `20` \
# d) `4, 5`
#
# ---
#
# ### 4. In Python, where should docstrings be placed in a function?
# a) After the function definition \
# b) Before the function definition \
# c) Immediately after the function signature \
# d) At the end of the function body
#
# ### 5. Which of these statements about Python functions is FALSE?
# a) Functions can return multiple values \
# b) Functions can have default parameter values \
# c) Function names should start with a number \
# d) Functions help reduce code duplication
#
# ---
#
# ### 6. Which of the following correctly describes how an `if` statement works?
# a) It executes code only when the condition is False \
# b) It executes code only when the condition is True \
# c) It always executes the code block regardless of condition \
# d) It requires at least two conditions to function
#
# ---
#
# ### 7. What will the following for loop print?
# ```
# for i in [1, 2, 3, 4, 5]:
#     print(f"{i} ")
# ```
# a) `['1', '2', '3', '4', '5'] ` \
# b) `'1 2 3 4 5'` \
# c) `1 2 3 4 5` \
# d)
#
# `1` \
# `2` \
# `3` \
# `4` \
# `5`
#
# ---
#
# ### Answers
# 1. **b**
# 2. **a**
# 3. **c**
# 4. **c**
# 5. **c**
# 6. **b**
# 7. **d**

#  Copyright (c) 2022 Mira Geoscience Ltd.
