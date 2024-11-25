import sys

# sys.argv is a list in Python that is used to handle command line arguments. When you run a script from the terminal any arguments you provide are stored in this list and access in the script.




def process_arguments(arguments):
    if len(arguments) > 1:
        print("Command line arguments:")
        for arg in arguments[1:]:
            print(arg)
    else:
        print("No command line arguments provided")

if __name__ == "__main__":
    # Pass command line arguments to the process_arguments function
    process_arguments(sys.argv)
