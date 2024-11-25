def square(x):
    return x ** 2

# Alias the square function
power_of_two = square

# Redefine the original function
def square(x):
    return x ** 2 + 1

# Now both functions exist, but they have different implementations
result_alias = power_of_two(3)  # Uses the original square function
result_new = square(3)  # Uses the redefined square function

print(result_alias)  # Output: 9 (3^2)
print(result_new)    # Output: 10 (3^2 + 1)
