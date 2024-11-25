from typing import Optional
import math

def greet(name: str) -> None: # The return type is None, which is optional
    """This function takes a name as a parameter (string) and prints a greeting."""
    print("Hello, " + name + "!")

def square_root(number: float) -> Optional[float]:# Optional is used to indicate that the return type can be None and it's a type hint from the typing module
    """
    This function takes a number as a parameter (float) and returns its square root (float).
    The return type is Optional[float], indicating that the result can be a float or None.
    """
    if number >= 0:
        return math.sqrt(number)
    else:
        return None

# Calling the greet function
greet("Alice")

# Calling the square_root function and printing the result
result: Optional[float] = square_root(25.0)# this line is specifying the type of the variable result which is float or None and we use ":" instead of "=" when specifying the type of a variable
if result is not None:
    print("Square root of 25:", result)
else:
    print("Cannot calculate square root of a negative number.")
