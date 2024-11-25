# Example of creating a set
fruits_set = {"apple", "banana", "orange", "apple", "kiwi"}

# Note: Duplicates are automatically eliminated
print("Set with duplicates removed:", fruits_set)

# Testing for membership
print("Is 'banana' in the set?", "banana" in fruits_set)
print("Is 'grape' in the set?", "grape" in fruits_set)

# Creating another set for set operations
more_fruits_set = {"kiwi", "grape", "watermelon", "banana"}

# Union of two sets
union_result = fruits_set.union(more_fruits_set)
print("Union of sets:", union_result)

# Intersection of two sets
intersection_result = fruits_set.intersection(more_fruits_set)
print("Intersection of sets:", intersection_result)

# Difference between two sets
difference_result = fruits_set.difference(more_fruits_set)
print("Difference between sets:", difference_result)

# Adding elements to a set
fruits_set.add("mango")
print("Set after adding 'mango':", fruits_set)

# Removing an element from a set
fruits_set.remove("kiwi")
print("Set after removing 'kiwi':", fruits_set)
