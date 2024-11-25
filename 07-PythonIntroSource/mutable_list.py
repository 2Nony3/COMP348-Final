# Original list
mutable_list = [1, 2, 3, 4, 5]

# Displaying the original list
print("Original List:")
print(mutable_list)

# Modifying elements in-place
mutable_list[1] = 10
mutable_list[2:4] = [30, 40]
mutable_list.append(6)

print("\nModified List:")
print(mutable_list)

# Removing elements in-place
del mutable_list[0]
mutable_list.remove(4)

print("\nList after Removal:")
print(mutable_list)

# Extending the list in-place
mutable_list.extend([7, 8, 9])

print("\nList after Extension:")
print(mutable_list)

# Reversing the list in-place
mutable_list.reverse()

print("\nReversed List:")
print(mutable_list)

# Sorting the list in-place
mutable_list.sort()

print("\nSorted List:")
print(mutable_list)

# Clearing the list in-place
mutable_list.clear()

print("\nCleared List:")
print(mutable_list)

# You may use sorted or reversed to leave the original list unchanged.