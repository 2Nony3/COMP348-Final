x = 42


def example_function():
    print(x)  # This would cause an UnboundLocalError if x were a local variable
    x = 45  # Assignment of x, TODO if we remove this line then it will take the global variable but since its we created a local value then the function will search for the local variable and it will not find it and it will throw an error


example_function()
