# --- Importing your custom module ---
import my_utils # Imports the entire my_utils.py file

# --- Importing standard library modules ---
import math
import random as rnd # Import with an alias

print("--- Using functions from my_utils module ---")
my_utils.greet("Students") # Call function using module_name.function()
area = my_utils.calculate_area_rectangle(5, 10)
print(f"Area of rectangle: {area}")

num_factorial = my_utils.factorial(5)
print(f"Factorial of 5: {num_factorial}")

print(f"PI value from my_utils: {my_utils.PI_VALUE}")

print("\n--- Using functions from math module ---")
sqrt_val = math.sqrt(25)
print(f"Square root of 25: {sqrt_val}")
print(f"Value of pi from math module: {math.pi}")

print("\n--- Using functions from random module (with alias) ---")
random_num = rnd.randint(1, 100) # Generate random integer between 1 and 100
print(f"Random number: {random_num}")

fruits = ["apple", "banana", "cherry", "date"]
random_fruit = rnd.choice(fruits) # Choose a random element from a sequence
print(f"Random fruit: {random_fruit}")

print("\n--- Importing specific items from a module ---")
from my_utils import greet, PI_VALUE # Import only greet and PI_VALUE directly

greet("Instructors") # Can call directly without my_utils.
print(f"PI_VALUE (directly imported): {PI_VALUE}")

# This will cause an error because calculate_area_rectangle was not directly imported
# calculate_area_rectangle(2,3) # Uncomment to see error
