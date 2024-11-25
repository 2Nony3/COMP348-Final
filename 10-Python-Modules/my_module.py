
def print_module_name():
    print("Module name:", __name__)

# Check if the script is the main program
if __name__ == "__main__":
    print("This script is the main program")
else:
    print("This script is being imported as a module")
