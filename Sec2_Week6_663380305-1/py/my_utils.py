def greet(name):
    """Prints a friendly greeting to the given name."""
    print(f"Hello, {name}! Welcome to my utility functions.")

def calculate_area_rectangle(length, width):
    """Calculates the area of a rectangle."""
    return length * width

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

PI_VALUE = 3.14159 # A constant defined in the module
