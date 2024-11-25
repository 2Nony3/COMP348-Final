# Creating a dictionary with various key types and values
my_dict = {
    'name': 'Alice',
    'age': 30,
    42: 'Answer to Everything',
    (1, 2): 'Tuple Key',
    'grades': {'math': 90, 'english': 85, 'science': 92}
}

# Accessing values using keys
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("Answer to Everything:", my_dict[42])
print("Tuple Key:", my_dict[(1, 2)])

# Accessing values in a nested dictionary
print("Math Grade:", my_dict['grades']['math'])
print("English Grade:", my_dict['grades']['english'])

# Modifying values
my_dict['age'] = 31
my_dict['grades']['science'] = 95

# Adding a new key-value pair
my_dict['city'] = 'Wonderland'

# Displaying the dictionary
print("\nUpdated Dictionary:")
print(my_dict)

# Removing a key-value pair
removed_value = my_dict.pop((1, 2))

# Displaying the dictionary after removal
print("\nDictionary after Removing Tuple Key:")
print(my_dict)

# Checking if a key exists
key_to_check = 'country'
if key_to_check in my_dict:
    print(f"\nThe value for '{key_to_check}' is: {my_dict[key_to_check]}")
else:
    print(f"\n'{key_to_check}' not found in the dictionary.")

# Iterating through keys and values
print("\nIterating Through Keys and Values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")
