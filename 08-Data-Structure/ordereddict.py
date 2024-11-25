#Starting from Python 3.7, the standard dict type in Python also maintains the order of insertion.
from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()

# Adding key-value pairs in a specific order
ordered_dict['one'] = 1
ordered_dict['three'] = 3
ordered_dict['two'] = 2

# Iterating over the items will maintain the insertion order
for key, value in ordered_dict.items():
    print(key, value)
