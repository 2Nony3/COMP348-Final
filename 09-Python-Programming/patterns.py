# Pattern 1: Incrementing
print("Pattern 1:")
for i in range(1, 6):
    print('*' * i)

# Pattern 2: Decrementing
print("\nPattern 2:")
for i in range(5, 0, -1):
    print('*' * i)

# Pattern 3: Right-angled Triangle
print("\nPattern 3:")
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * i)

# Pattern 4: Pyramid
print("\nPattern 4:")
for i in range(1, 6):
    print(' ' * (5 - i) + '*' * (2 * i - 1))

# Pattern 5: Hollow Square
print("\nPattern 5:")
size = 5
for i in range(size):
    if i == 0 or i == size - 1:
        print('*' * size)
    else:
        print('*' + ' ' * (size - 2) + '*')
