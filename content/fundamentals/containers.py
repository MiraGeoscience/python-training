#%% md
# # Containers
# 
# In the previous section, we introduced numeric types such as `int` and `float`, as well as text variables (`str`). Often, we want to group multiple values together in order to perform larger or more complex operations.
# 
# This section introduces built-in container types in Python, which allow you to store and organize multiple related values in a single variable.
# 
#%% md
# ## List
# 
# Lists are ordered collections that can store multiple items of any type (even mixed types). They are created using square brackets `[]` with comma-separated values.
#%%
a_list = [1.0, 2, "abc"]
print(a_list)
print(type(a_list))
#%% md
# ### Common List Operations
# 
# - **Indexing**: Access elements in the list using their position (index). In Python, indexing starts at 0, not 1.
#%%
# Access the first element (index 0)
first_element = a_list[0]
print("First element:", first_element)

# Access the second element (index 1)
second_element = a_list[1]
print(f"Second element: {second_element}")
#%% md
# - **Adding elements**: You can add items to a list using the `append()` method or the `+=` operator.
#%%
# Using append() method to add a single item
a_list.append("new item")
print("After append:", a_list)

# Using += operator to add another list
a_list += ["another item"]
print("After +=:", a_list)
#%% md
# - **Removing elements**: You can remove items using the `pop()` method by specifying the index.
#%%
# Remove the first element (index 0)
removed_item = a_list.pop(0)
print(f"Removed item: {removed_item}")
print(f"List after removal: {a_list}")
#%% md
# - **Finding elements**: Use the `index()` method to find the position of an
# item in the list. This also works for strings, as they are also sequences
# (but not exactly the same as lists).
#%%
# Find the index of "abc" in the list
position = a_list.index("abc")
print(f"'abc' is at index: {position} in the list")

# Find the index of the first "i" in the string
my_string = "This is a string"
position_in_string = my_string.index("i")
print(f"'i' is at index: {position_in_string} in the string")
#%% md
# - **List length**: You can check how many items are in a list using the `len()` function.
#%%
list_length = len(a_list)
print(f"The list contains {list_length} items")
#%% md
# ## Dictionary
# 
# Dictionaries (`dict`) are also containers for objects but give an additional level of structure over lists as every
# value of the dictionary is indexed by a `key`. A dictionary is created with a list of `key: value` pairs within
# braces `{}`.
#%%
my_dict = {"integer": 2, "name": "Jane Doe"}
print(my_dict)
#%% md
# ### Common Dictionary Operations
# 
# - **Accessing values**: Use the key inside square brackets to access values.
#%%
# Get the value for key "integer"
value = my_dict["integer"]
print(f"Value for key 'integer': {value}")
#%% md
# - **Adding or updating entries**: Assign a value to a new key to add it, or to an existing key to update it.
#%%
# Add a new entry
my_dict["new"] = 123
print("After adding 'new':", my_dict)

# Update an existing entry
my_dict["integer"] = 5
print("After updating 'integer':", my_dict)
#%% md
# - **Removing entries**: Use the `del` keyword to remove a key-value pair.
#%%
# Remove the "new" entry
del my_dict["new"]
print("After removing 'new':", my_dict)
#%% md
# - **Getting all keys**: You can get a view of all keys in the dictionary.
#%%
# Get all keys
all_keys = list(my_dict)
print("All keys:", all_keys)
#%% md
# - **Getting all values**: Similarly, you can access all values.
#%%
# Get all values
all_values = list(my_dict.values())
print("All values:", all_values)
#%% md
# - **Getting all key-value pairs**: You can access all key-value pairs as
# tuples. A **tuple** is an immutable sequence type, similar to a list, but it cannot be changed after creation.
#%%
# Get all key-value pairs
all_items = list(my_dict.items())
print("All key-value pairs:", all_items)
#%% md
# - **Checking if a key exists**: Use the `in` keyword to check if a key is
# present in the dictionary. You can also do this to check for values in a list
#  or string.
#%%
print("Is 'name' in my_dict?", "name" in my_dict)
#%% md
# ## Knowledge Check: Python Containers
# 
# ### 1. If you create a list `numbers = [10, 20, 30, 40]`, what is the value of `numbers[2]`?
# a) 10 \
# b) 20 \
# c) 30 \
# d) 40
# 
# ### 2. Which of these correctly adds the value `50` to the end of the list `numbers`?
# a) `numbers + 50` \
# b) `numbers.add(50)` \
# c) `numbers.append(50)` \
# d) `numbers[4] = 50`
# 
# ### 3. How would you create a dictionary with keys 'name' and 'age' with corresponding values 'Alice' and 30?
# a) `{'name', 'Alice', 'age', 30}` \
# b) `{'name': 'Alice', 'age': 30}` \
# c) `['name', 'Alice', 'age', 30]` \
# d) `('name', 'Alice', 'age', 30)`
# 
# ### 4. What is the result of `len([1, 2, 3, 4, 5])`?
# a) 4 \
# b) 5 \
# c) 6 \
# d) It depends on what the numbers are
# 
# ### Answers
# 1. c
# 2. c
# 3. b
# 4. b
#%% md
#  Copyright (c) 2022 Mira Geoscience Ltd.