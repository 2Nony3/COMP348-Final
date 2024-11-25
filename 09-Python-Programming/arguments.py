# Function with default arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Function with named arguments
def describe_pet(animal_type, pet_name, age=None):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

    if age is not None:
        print(f"{pet_name} is {age} years old.")

# Using functions with default arguments
greet("Alice")  # Uses the default greeting
greet("Bob", "Good morning")  # Uses the provided greeting

# Using function with named arguments
describe_pet(animal_type="Dog", pet_name="Buddy")
describe_pet("Cat", "Whiskers", age=3)
