import my_module

# Call the function from the imported module
my_module.print_module_name()

# Check if this script is the main program
if __name__ == "__main__":
    print("This script is the main program")
else:
    print("This script is being imported as a module")
