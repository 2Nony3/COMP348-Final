# Creating a tuple
my_tuple = (1, 2, 3, 'hello', [4, 5])

# Accessing elements in a tuple
print("Original Tuple:", my_tuple)
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

# Trying to modify a tuple (this will raise an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")

# Modifying a mutable element inside a tuple
my_tuple[-1][0] = 99
print("Modified Tuple:", my_tuple)
