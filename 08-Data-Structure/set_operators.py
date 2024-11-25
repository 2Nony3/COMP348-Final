# Define two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1 | set2
print("Union:", union_set)

# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)

# Difference
difference_set1 = set1 - set2
difference_set2 = set2 - set1
print("Difference (set1 - set2):", difference_set1)
print("Difference (set2 - set1):", difference_set2)

# Symmetric Difference
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference:", symmetric_difference_set)

# Subset and Superset
is_subset = set1 <= set2
is_superset = set1 >= set2
print("Is set1 a subset of set2:", is_subset)
print("Is set1 a superset of set2:", is_superset)
