# Original string
original_string = "HelloWorld"

# Basic slicing
slice_1 = original_string[1:5]  # from index 1 to 4 (exclusive)
slice_2 = original_string[5:]   # from index 5 to the end
slice_3 = original_string[:5]   # from the beginning to index 4
slice_4 = original_string[-3:]  # last 3 characters
slice_5 = original_string[2:-2] # from index 2 to (last character - 2)

# Creating a new string by concatenation
new_string = original_string[:6] + " Python!"

# Displaying the results
print("Original String:", original_string)
print("Slice 1:", slice_1)
print("Slice 2:", slice_2)
print("Slice 3:", slice_3)
print("Slice 4:", slice_4)
print("Slice 5:", slice_5)
print("New String:", new_string)
