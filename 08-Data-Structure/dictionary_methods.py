# Creating a dictionary
my_dict = {'one': 1, 'three': 3, 'two': 2}

# Printing the original dictionary
print("Original Dictionary:")
print(my_dict)

# Using dict.items() to get key/value pairs
print("\nKey/Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Using dict.keys() to get a list of keys
print("\nKeys:")
keys_list = my_dict.keys()
print(keys_list)

# Using dict.values() to get a list of values
print("\nValues:")
values_list = my_dict.values()
print(values_list)

# Using dict.clear() to remove all items
my_dict.clear()
print("\nDictionary after clear:")
print(my_dict)

# Using dict.get(key) to get a value by key (without raising an error if the key doesn't exist)
# The 'key not found' is the default value that dict.get(key) returns if the specified key is not found in the dictionary. 
# The method dict.get(key, default) takes two arguments:
print("\nUsing dict.get(key):")
value_for_key = my_dict.get('three', 'Key not found')
print(f"Value for 'three': {value_for_key}")

# Attempting to access a key that doesn't exist directly would raise a KeyError
# Uncomment the next line to see the KeyError
# value_for_invalid_key = my_dict['invalid_key']

# Note: Uncomment the above line to see the KeyError if you want to observe the difference
