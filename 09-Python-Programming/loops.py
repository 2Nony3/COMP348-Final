# For Loop
print("For Loop:")
for i in range(1, 6):
    print(i, end=' ')  # Prints numbers 1 to 5
print("\n")

# While Loop
print("While Loop:")
count = 1
while count <= 5:
    print(count, end=' ')  # Prints numbers 1 to 5
    count += 1
print("\n")

# Do-While Equivalent
print("Do-While Equivalent:")
count = 1
while True:
    print(count, end=' ')  # Prints numbers until count becomes greater than 5
    count += 1
    if count > 5:
        break
print("\n")

# Using Continue
print("Using Continue:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i, end=' ')
print("\n")
