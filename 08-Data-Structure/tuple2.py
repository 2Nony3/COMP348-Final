# Creating tuples with different elements
empty_tuple = ()
single_element_tuple = 42,  # Note the trailing comma
simple_tuple = 1, 2, 3,
nested_tuple = ('a', (4, 5), [6, 7])

# Displaying the tuples
print("Empty Tuple:", empty_tuple)
print("Single Element Tuple:", single_element_tuple)
print("Simple Tuple:", simple_tuple)
print("Nested Tuple:", nested_tuple)

# Accessing elements in a nested tuple
print("Accessing Nested Tuple Element:", nested_tuple[1][0])

# Creating a tuple without parentheses (also valid)
another_tuple = 10, 20, 30
print("Tuple Without Parentheses:", another_tuple)