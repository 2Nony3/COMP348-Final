# Original list
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic slicing
slice_1 = original_list[1:5]  # from index 1 to 4 (exclusive)
slice_2 = original_list[5:]   # from index 5 to the end
slice_3 = original_list[:5]   # from the beginning to index 4
slice_4 = original_list[-3:]  # last 3 elements
slice_5 = original_list[2:-2] # from index 2 to (last element - 2)

# Creating a new list by concatenation
new_list = original_list[:6] + [100, 200, 300]

# Displaying the results
print("Original List:", original_list)
print("Slice 1:", slice_1)
print("Slice 2:", slice_2)
print("Slice 3:", slice_3)
print("Slice 4:", slice_4)
print("Slice 5:", slice_5)
print("New List:", new_list)
