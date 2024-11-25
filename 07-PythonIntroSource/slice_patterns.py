# Original string
original_string = "PythonProgrammingIsFun"

# Extracting odd indices in forward order
odd_forward = original_string[1::2]

# Extracting even indices in forward order
even_forward = original_string[0::2]

# Extracting odd indices in reverse order
odd_reverse = original_string[-2::-2]

# Extracting even indices in reverse order
even_reverse = original_string[-1::-2]

# Displaying the results
print("Original String:", original_string)
print("Odd Indices (Forward):", odd_forward)
print("Even Indices (Forward):", even_forward)
print("Odd Indices (Reverse):", odd_reverse)
print("Even Indices (Reverse):", even_reverse)
