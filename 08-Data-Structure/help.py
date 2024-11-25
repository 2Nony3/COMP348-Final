my_list = []  # Replace this with your list

# Get all available attributes (including methods) of the list
all_attributes = dir(my_list)

# Filter out non-callable attributes (methods)
methods_only = [attr for attr in all_attributes if callable(getattr(my_list, attr)) and not attr.startswith('_')]

# Print help information for each method
for method in methods_only:
    print(f"\nHelp for method: {method}")
    help(getattr(my_list, method))
