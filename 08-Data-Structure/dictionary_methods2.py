# Creating a dictionary
my_dict = {'one': 1, 'two': 2, 'three': 3}
print("Original Dictionary:", my_dict)

# Deleting a key
del my_dict['two']
print("Dictionary after deleting 'two':", my_dict)

# Checking for existence
key_to_check = 'three'
if key_to_check in my_dict:
    print(f"'{key_to_check}' exists in the dictionary.")
else:
    print(f"'{key_to_check}' does not exist in the dictionary.")

# Length of dictionary
print("Number of items in the dictionary:", len(my_dict))

# Adding or updating a key
my_dict['four'] = 4
print("Dictionary after adding 'four':", my_dict)

# Updating the value of an existing key
my_dict['one'] = 10
print("Dictionary after updating 'one':", my_dict)

# Using get() to avoid KeyError
value_for_key = my_dict.get('five', 'Key not found')
print(f"The value for 'five': {value_for_key}")
