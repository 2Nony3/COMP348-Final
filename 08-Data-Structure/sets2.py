# Approach 1: Using curly braces
fruits_set = {"apple", "orange", "banana"}

# Approach 2: Using set() function
colors_set = set(["red", "green", "blue"])

# Adding elements to a set
fruits_set.add("kiwi")
colors_set.add("yellow")

# Displaying the initial sets
print("Fruits Set:", fruits_set)
print("Colors Set:", colors_set)

# Removing an element from a set
fruits_set.remove("apple")

# Displaying the modified sets
print("Fruits Set after removing 'apple':", fruits_set)

# Clearing all elements from a set
colors_set.clear()

# Displaying the empty set
print("Colors Set after clearing:", colors_set)

# Using discard() to remove an element
fruits_set.discard("banana")
print("Fruits Set after discarding 'banana':", fruits_set)
