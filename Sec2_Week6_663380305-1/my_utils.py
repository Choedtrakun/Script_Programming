# my_utils.py (Custom Module)

def greet(name: str):
    """Prints a greeting message to the given name."""
    print(f"Hello, {name}!")

def is_prime(number: int) -> bool:
    """Returns True if the number is prime, False otherwise."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True