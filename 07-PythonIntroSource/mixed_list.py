# Creating a mixed list
mixed_list = [1, "apple", 3.14, True, [5, 6, 7], {"name": "John", "age": 25}]

# Displaying the original mixed list
print("Original Mixed List:")
print(mixed_list)

# Accessing and modifying elements
print("\nAccessing and Modifying Elements:")
print("Element at index 1:", mixed_list[1])
print("Element at index 4, sub-list element at index 1:", mixed_list[4][1])

mixed_list[2] = "banana"
mixed_list[4][0] = 99
mixed_list[5]["city"] = "New York"

print("Modified Mixed List:")
print(mixed_list)

# Adding and removing elements
print("\nAdding and Removing Elements:")
mixed_list.append(False)
mixed_list.insert(2, "cherry")
mixed_list.remove(3.14)

print("After Adding and Removing:")
print(mixed_list)

# Slicing and combining lists
print("\nSlicing and Combining Lists:")
sliced_portion = mixed_list[1:4]
new_list = [8, 9, 10]
combined_list = mixed_list + new_list

print("Sliced Portion:", sliced_portion)
print("Combined List:", combined_list)

# Checking for elements
print("\nChecking for Elements:")
print("Is 'apple' in the list?", 'apple' in mixed_list)
print("Is 'grape' not in the list?", 'grape' not in mixed_list)

# Displaying the final mixed list
print("\nFinal Mixed List:")
print(mixed_list)
