#%% md
# # Python Fundamentals
# 
# Almost all computer programs can be broken down into simple operations that
# are stringed together to perform complex tasks. In this section, we introduce
# core Python concepts and syntax that are required to write Python programs.
#%% md
# ## Variables
# 
# A key component of programming is the storage of information in computer
# memory as **variables**. Variables are a way to assign human-readable labels
# to blocks of data. We will start with simple **numerical** and **string**
# variables.
# 
# ## Numerics
# 
# Numerical values can be of type `float` (numbers with decimals) or of type
# `int`
# (integers). Floats are mainly used for
# arithmetic while integers are commonly used to count or index arrays. Let's
# create a variable:
#%%
x = 1
x
#%% md
# We have created our first numerical variable, **x**, which the computer
# stores as
#  a pointer to the `int` value of **1**.
# 
#%% md
# Now let's create a second variable **y** of numerical type `float`. This is done by assigning **y** any number containing a decimal point:
#%%
y = 1.0
y
#%% md
# ## Everything Has a Type
# 
# In Python, every value has a **type**. The type tells Python what kind of object it is and what operations can be performed on it.
# 
# You can check the type of any object using the built-in `type()` function:
#%%
type(x)
#%% md
# You may have noticed that you can get the value or output of an expression (e.g., `x` or `type(x)`) by having that expression as the last one in a Code Cell. However, there are many situations where you will need to use the `print()` function to get outputs. For instance, if you would like more than one output from a single cell. Note that in the first cell below, only the last statement produces an output, whereas in the second cell below, you get an output from every line:
#%%
x
type(x)
x + 1
#%%
print(x)
print(type(x))
x + 1
#%% md
# ## Comments in Python
# 
# **Comments** are lines in your code that Python ignores when running the program. You can use comments to explain what your code is doing, leave notes for yourself, or help others understand your code.
# 
# In Python, a comment starts with the `#` symbol. Everything after `#` on that line is treated as a comment and not executed.
# 
# Here’s an example:
# 
#%%
# This is a comment
x = 5  # Assign the value 5 to the variable x

# Add 5 to x, then print the result
x = x + 5
print(x)
#%% md
# ## Operations
# 
# Here is a short list of standard arithmetic and logical operators that can be applied on numerical values (in order
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
#%%
# This expression is True
2**2 * 1.5 + 1 == 7.0
#%%
(5 * 5) % 10 > 6 # Modulo gives the remainder of a division operation. Since 25 % 10 is 5, this expression is False
#%% md
# You can verify the results above by doing the operations in your head.
# 
# It is important to keep in mind general rules
# of return types for numerical values:
# 
# - Adding or subtracting integers yields an integer:
#%%
type(x + x)
#%% md
# - Multiplying or dividing integers yields a float:
#%%
type(x / x)
#%% md
# - An operation working with both and integer and a float will always yield a float:
#%%
type(x + y)
#%% md
# ## Strings
# 
# Strings (`str`) are text objects that contain characters (letters, numbers or
# symbols) surrounded by single `''` or double
# `""` quotes. Both are acceptable but consistency throughout your code is preferable.
# 
# 
#%%
my_string = "This is a string"
type(my_string)
#%%
my_string
#%% md
# Here is a short list of useful methods that can be used on strings.
# 
# - Adding:
#%%
"hello" + " world"
#%% md
# - Making strings uppercase/lowercase, or capitalizing their first character:
#%%
"I".lower() + " love ".upper() + "python".capitalize()
#%% md
# - Capitalizing the first letter of every word:
#%%
"this is important".title()
#%% md
# - Creating a formatted string ("f-string") to add variables into text:
#%%
name = "Python"
greeting = f"Hello, {name}!"
print(greeting)
#%% md
# ## Objects
# 
# At its core, Python is an **object-oriented programming (OOP)** language. 
# 
# In simple terms, a Python computer program is made up of many **objects**, which are variables that can store data (**attributes**) and perform actions (**methods**). An **object** is created from something called a **class**, which acts like a blueprint for the object.
# 
# You can think of an object like a small machine: it can take input, store information, and perform tasks when asked. Objects can also work together to create more complex programs.
# 
# Object-oriented programming helps make code shorter, easier to read, and easier to share — which is one reason Python is so popular, especially in open-source projects.
# 
# 
# ![oop](./images/object_oriented.png)
# 
# This is somewhat different from **imperative** or **procedural-based** languages, such as **C** and **Fortran**. In an imperative approach, variables and functions are connected to form a sequence of steps that the computer follows. However, in this model, variables are just simple containers for data — they don't have any built-in behavior.
# 
# ![imperative](./images/imperative.png)
# 
# While Python can also be written in a procedural style, behind the scenes, objects are always doing the work.
# 
# For example, consider the numeric variable `x` introduced earlier. Even though it may look like a simple integer, `x` is actually a Python object with its own methods. In a Jupyter Notebook, you can see the available methods for `x` by typing a dot (`.`) after the variable name, then pressing the `Tab` key.
# 
# ![methods](./images/methods.png)
# 
# In this case, one of the methods, `imag`, would return the imaginary part of `x` (if it were a complex number).
# 
# Later, in the section on [Classes](classes), you will learn how to create your own brand-new types of objects with custom methods! 
# 
#%% md
# ## A Note on Literals vs Variables
# 
# When you write values like `42`, `3.14`, or `"hello"` directly in your code, these are called **literals**. 
# 
# When you assign a literal to a name, you create a **variable** that refers to the object:
#%%
x = 42 # "42" is a literal; "x" is a variable
#%% md
# A variable is simply a name that points to an object stored in memory. You can reuse the same name to refer to different objects later:
#%%
x = 3.14 # now "x" refers to a float object
print("x now equals:", x)
#%% md
# ## Summary: What You've Learned
# 
# - **Python is an object-oriented language**. Everything in Python is an object.
# - An **object** is a value that can store information (**attributes**) and perform actions (**methods**).
# - **Variables** are names that refer to objects in memory, whereas **Literals** are raw values written directly in code, like `42` or `"hello"`.
# - You can check the **type** of any object using the built-in `type()` function.
# - You can print values/objects to the output using the `print()` function.
# - You wrote and explored code interactively using variables, types, and basic object behavior.
# - You learned how to write **comments** to explain your code and make it easier to read.
# 
# It is recommended to confirm your knowledge of the concepts covered in this section, as new concepts will build on what you've already learned. You are encouraged to experiment by creating code cells and writing your own code, or editing the code in existing code cells. 
# 
# Then, try the short quiz below to test your understanding.
# 
#%% md
# ## Knowledge Check: Python Fundamentals (Answers at the end)
# 
# ### 1. Which of the following best describes a Python object?
# 
# a) A piece of text used to document code  
# b) A data value that can store information and have associated behavior  
# c) A function that modifies variables  
# d) A number stored in memory
# 
# ---
# 
# ### 2. What does the `type()` function return?
# 
# a) The memory address of a variable  
# b) The function signature of a method  
# c) The class name of the object  
# d) The data content of a variable
# 
# ---
# 
# ### 3. What is the difference between a literal and a variable?
# 
# a) A literal is the name of a variable  
# b) A variable is the raw data stored in memory, and a literal is a Python object  
# c) Unlike in languages like C and Fortran, there is no difference between the two in Python  
# d) A literal is a fixed value written in code, and a variable is a name referring to that value  
# 
# 
# ---
# 
# ### 4. Which of the following statements about object-oriented programming in Python is correct?
# 
# a) Python only uses objects when explicitly told to do so  
# b) Only custom classes are considered objects  
# c) Everything in Python, including numbers and strings, is treated as an object  
# d) Variables in Python do not have types
# 
# ---
# 
# ### 5. What symbol is used to write a comment in Python?
# 
# a) `//`  
# b) `#`  
# c) `--`  
# d) `;`
# 
# ---
# 
# ### 6. Which of the following lines correctly assigns the value 3.14 to a variable?
# 
# a) `3.14 = pi`  
# b) `pi <- 3.14`  
# c) `pi = 3.14`  
# d) `float pi = 3.14`  
# 
# ---
# 
# ### 7. What will the following code print?
# 
# ```
# x = 7
# y = 5.0
# z = 5 + x * y
# print(z)
# ```
# 
# a) `40.0`  
# b) `60.0`  
# c) `<class 'int'>`  
# d) `40`
# 
# ---
# 
# ### 8. Given the code below, what value is printed?
# 
# ```
# a = 4
# b = 3
# print(a + b)
# ```
# 
# a) `7`  
# b) `43`  
# c) `a + b`    
# d) `None`  
# 
# --- 
# 
# ### Answers
# 
# 1. **b**  
# 2. **c**  
# 3. **d**  
# 4. **c**  
# 5. **b**
# 6. **c**
# 7. **a**
# 8. **a**
# 
#%% md
# You're now ready to move on to **containers**, **functions**, and eventually creating your own **classes**!
#%% md
#  Copyright (c) 2022 Mira Geoscience Ltd.