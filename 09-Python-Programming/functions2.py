from typing import Optional
import math

def greet(name: str) -> None:
    """This function takes a name as a parameter (string) and prints a greeting."""
    print("Hello, " + name + "!")

def square_root(number: float) -> Optional[float]:
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
result: Optional[float] = square_root(25.0)
if result is not None:
    print("Square root of 25:", result)
else:
    print("Cannot calculate square root of a negative number.")
