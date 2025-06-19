#%% md
# # Classes
# 
# While `functions` are common to almost all types of programming languages, the concept of `Class` is specific to object-oriented languages. Classes let you create your own custom object types that can contain both data (attributes) and behavior (methods).
# 
# In this section, we'll learn how classes help organize code in a more structured way compared to using separate functions and variables.
# 
#%% md
# ## Why Use Classes?
# 
# Let's revisit the assay analysis from the previous [Functions](Functions) section. We had two lists for `grades` and `depths`, and we wanted to find depths where values exceeded some threshold.
#%%
grades = [0.1, 0.02, 1.3, 2.4, 3.5, 0.01]
depths = [10, 55, 80, 105, 115, 120]
#%% md
# ## Creating a Class
# 
# Let's create an `Assay` class that brings together the data (grades and depths) and the functions we created previously:
#%%
class Assay:
    """Simple Assay class that stores and analyzes grade measurements at different depths."""

    def __init__(self, arg_1: list, arg_2: list, threshold: float = 1.0):
        self.grades = arg_1
        self.depths = arg_2
        self.threshold = threshold

    def anomalous(self):
        """
        Find the elements of a list above threshold.
        
        :return: A list of True/False values indicating which grades exceed the threshold
        """
        return [val > self.threshold for val in self.grades]

    def get_depths(self):
        """
        Extract depths where grades exceed the threshold.
        
        :return: A list of depths where grades are above the threshold
        """
        output = []
        for val, cond in zip(self.depths, self.anomalous()):
            if cond:
                output.append(val)
        return output

    def __call__(self):
        return self.get_depths()
#%% md
# ## Class Anatomy
# 
# Let's break down the components of our class:
# 
# ### `class` Keyword
# 
# The `class` keyword tells Python we're creating a new object type, followed by the name of the class (typically using CamelCase, where each word starts with a capital letter).
#%% md
# ### `__init__` Method (Constructor)
# 
# The `__init__` method is special - it runs automatically when we create a new instance of the class. It's like a setup function that prepares our object with initial values:
# 
# ```python
# def __init__(self, arg_1: list, arg_2: list, threshold: float = 1.0):
#     self.grades = arg_1
#     self.depths = arg_2
#     self.threshold = threshold
# ```
# 
# - `self` refers to the specific instance of the class being created
# - The other parameters are values we want to provide when creating the object
# - We store the values as attributes of the object using `self.attribute_name`
# 
# ### Creating an Instance
# 
# To create an instance of our class (an actual object), we call the class name like a function:
#%%
# Create a new Assay object
assay = Assay(grades, depths)

# What type of object is it?
print(f"Type of 'assay': {type(assay)}")
#%%
# Accessing its attributes
print(f"First few grades: {assay.grades[0:3]}") # get items in indices 0, 1, 2 of the list 'assay.grades' using `[0:3]`
print(f"Default threshold: {assay.threshold}")
#%% md
# ### The `self` Parameter
# 
# The self parameter is a reference to the current instance of the class. It:
# 
# - Must be the first parameter of every method in the class
# - Allows methods to access and modify the object's attributes
# - Lets methods call other methods within the same object
# 
# For example, in our anomalous() method:
# ```python
# def anomalous(self):
#     return [val > self.threshold for val in self.grades]
# ```
# 
# The method uses `self` to access the `threshold` and `grades` attributes we defined in `__init__`.
#%%
# Calling a method of our object
high_grade_locations = assay.anomalous() 

print("Is each sample above the threshold?")
print(high_grade_locations)
#%% md
# ### Methods vs Functions
# Methods are functions that belong to a class. The main differences are:
# 
# 
# 1. Methods are defined inside a class
# 2. Methods always take `self` as their first parameter
# 3. Methods are called using the dot notation on an object: `object.method()`
#%% md
# ## The  `__call__` Method
# 
# The `__call__` method lets you use your object as if it were a function. When you add parentheses after your object name (like `assay()`), Python looks for a `__call__` method to execute.
# 
# In our case, we defined `__call__` to run the `get_depths()` method:
# 
# ```python
# def __call__(self):
#     return self.get_depths()
# ```
# 
# This gives us a handy shortcut:
#%%
# These two lines do the same thing:
print("Using the get_depths method:", assay.get_depths())
print("Using the __call__ method:", assay())
#%% md
# ## Properties and Attribute Control
# 
# Sometimes we want to add validation or special behaviour when getting or setting attributes. Python's `@property` decorator lets us do this:
#%%
class Assay2: 
    """
    Improved Assay class with property validation.
    """
    
    def __init__(self, arg_1: list, arg_2: list, threshold: float = 1.0):
        self.grades = arg_1
        self.depths = arg_2
        self._threshold = threshold  # Note the underscore
    
    def anomalous(self):
        """
        Find the elements of a list above threshold.
        """
        return [val > self.threshold for val in self.grades]
    
    def get_depths(self):
        """
        Extract depths where grades exceed the threshold.
        """
        output = []
        for val, cond in zip(self.depths, self.anomalous()):
            if cond:
                output.append(val)
        return output
    
    @property
    def threshold(self) -> float:
        """Cutoff value for anomalous assays."""
        return self._threshold  # Note: accessing _threshold, not threshold
    
    @threshold.setter
    def threshold(self, value):
        """Validate threshold value when it's changed."""
        if not isinstance(value, float):
            raise ValueError("The value for threshold must be a float.")
    
        self._threshold = value
    
    def __call__(self):
        return self.get_depths()
#%% md
# ### Private Attributes with Underscores
# 
# In Python, adding a single underscore before an attribute name (like `_threshold`) is a convention that indicates this attribute should be considered "private" or "internal" to the class:
# 
# - It signals to other developers: "please don't access this directly from outside the class"
# - It's not enforced by Python (unlike in other langauges), but it's a widely respected convention
# - It helps prevent accidental changes to important internal variables
#%% md
# ### Property Decorators
# 
# The `@property` decorator transforms a method into an attribute-like accessor. This gives you control over how attributes are accessed:
# ```python
# @property
# def threshold(self) -> float:
#     """Cutoff value fo anomalous assays."""
#     return self._threshold 
# ```
# 
# When someone accesses `assay.threshold`, this method runs and returns the value.
# 
# The `@threshold.setter` decorator creates a method that runs when someone tries to change the attribute:
# ```python
# @threshold.setter
# def threshold(self, value):
#     """Validate threshold value when it's changed."""
#     if not isinstance(value, float):
#         raise ValueError("The value for threshold must be a float.")
#   
#     self._threshold = value
# ```
# 
# This lets us validate the new value before accepting it:
#%%
# Create our improved assay
assay2 = Assay2(grades, depths)

# This works fine because 2.0 is a float
assay2.threshold = 2.0 
print(f"New threshold: {assay2.threshold}")

# This would raise an error because it's not a float
# assay2.threshold = "high" # uncomment to see error
#%% md
# ## When to Use Classes
# 
# Classes are most useful when:
# 
# - You have data and behaviour that logically belong together
# - You want to create multiple similar objects with the same structure
# - You want to maintain state of an object across multiple operations
# - You want to organize related functionality into a single unit
# - You're building a larger system where code organization is important
# 
# For simple scripts or one-off tasks, functions might be simpler. But as your programs grow in complexity, classes help keep your code organized and maintainable.
#%% md
# ## Summary: What You've Learned
# 
# Classes are a fundamental feature of object-oriented programming that allow you to create your own custom data types. While functions help organize code into reusable blocks, classes go further by combining related data (attributes) and behavior (methods) into a single unit.
# 
# In this notebook, you learned:
# 
# 
# - **Classes** are blueprints for creating objects with **attributes** (data) and **methods** (behavior)
# - The `class` keyword defines a new class in Python
# - The `__init__` method initializes new objects when they're created
# - `self` refers to the current instance and must be the first parameter in instance methods
# - Classes help organize related data and behavior in a more structured way
# - `Objects` are instances of classes that store their own state
# - `Methods` are functions that belong to a class and can access/modify its attributes
# - Object-oriented programming helps keep code organized, reusable, and maintainable
# 
# By using classes, you can create custom data types specific to your problem domain, making your code more intuitive and easier to maintain.
# 
# 
#%% md
# 
# ## Knowledge Check: Python Classes
# 
# ### 1. What keyword is used to define a class in Python?
# 
# a) `struct`     
# b) `def`  
# c) `object`  
# d) `class`  
# 
# ---
# 
# ### 2. What is the purpose of the `__init__` method in a class?
# a) To delete an object when it's no longer needed  
# b) To initialize a new object with attributes when it's created  
# c) To import required modules for the class  
# d) To define which methods can be accessed from outside the class  
# 
# ---
# 
# ### 3. What does the `self` parameter refer to in a class method?
# a) The class itself   
# b) The method being called   
# c) The current instance of the class   
# d) The attribute assigned to `self` in the class definition
# 
# ---
# 
# ### 4. How do you create an instance of a class named Student?
# a) `Student.create()`   
# b) `Student(self)`   
# c) `Student()`   
# d) `Student.__init__()`
# 
# ---
# 
# ### 5. In object-oriented programming, what are attributes?
# a) The names of classes in your program \
# b) The data or variables that belong to an object \
# c) The keywords used to define a class \
# d) The modules required by a class
# 
# ---
# 
# ### 6. What's the main benefit of using classes instead of separate functions and variables?
# a) Classes organize related data and behavior together \
# b) Classes use less memory than functions \
# c) Classes always execute faster than functions \
# d) Classes allow you to execute multiple functions at once
# 
# ---
# 
# ### 7. Which of the following is true about methods in a class?
# a) Methods always require at least two parameters  
# b) Methods always require exactly one parameter   
# c) Methods can access and modify object attributes using `self`  
# d) Methods must always return a value  
# 
# ---
# 
# ### Answers
# 1. d
# 2. b
# 3. c
# 4. c
# 5. b
# 6. a
# 7. c
#%% md
#  Copyright (c) 2022 Mira Geoscience Ltd.