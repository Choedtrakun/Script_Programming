# main_program.py
import math
import random
import my_utils

def main():
    # Call my_utils.greet()
    my_utils.greet("Alice")

    # Test my_utils.is_prime() with test numbers
    test_numbers = [7, 10, 13, 1]
    for num in test_numbers:
        print(f"Is {num} prime? -> {my_utils.is_prime(num)}")

    # Use math.sqrt() to calculate square root
    sqrt_val = math.sqrt(64)
    print(f"Square root of 64: {sqrt_val}")

    # Use random.randint() to generate a random integer between 1 and 100
    random_val = random.randint(1, 100)
    print(f"Random integer (1-100): {random_val}")

if __name__ == "__main__":
    main()