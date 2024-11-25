s1 = "bigdog"
memory_address_before = id(s1)

# Attempting to modify the string
# This will create a new string object and assign it to s1
s1 = s1[:2] + "G" + s1[3:]

memory_address_after = id(s1)

print("Memory Address Before Modification:", memory_address_before)
print("Memory Address After Modification:", memory_address_after)