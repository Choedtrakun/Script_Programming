print("--- Basic Function Definition and Call ---")
def greet():
    """Prints a simple greeting."""
    print("Hello from a function!")

greet() # Calling the function
greet() # Call it again! Code reuse!

print("\n--- Functions with Parameters and Arguments ---")
def personalized_greet(name):
    """Greets the user by their provided name."""
    print(f"Hello, {name}!")

personalized_greet("Alice") # Positional argument
personalized_greet("Bob")

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"Its name is {pet_name}.")

describe_pet("dog", "Buddy") # Positional arguments
describe_pet(pet_name="Whiskers", animal_type="cat") # Keyword arguments (order doesn't matter)

print("\n--- Functions with Default Parameter Values ---")
def make_coffee(size="regular", type="latte"):
    """Describes a coffee order with default values."""
    print(f"Making a {size} {type} coffee.")

make_coffee() # Uses defaults: regular latte
make_coffee("large") # Uses default type: large latte
make_coffee(type="espresso", size="small") # Custom order: small espresso

print("\n--- Functions with Return Values ---")
def add_numbers(num1, num2):
    """Adds two numbers and returns their sum."""
    sum_result = num1 + num2
    return sum_result # Return the value

result = add_numbers(10, 5)
print(f"Sum of 10 and 5: {result}")

def get_circle_area(radius):
    """Calculates and returns the area of a circle."""
    import math # Local import (can be done, but usually at top of file)
    area = math.pi * (radius ** 2)
    return area

radius_val = 7
area_val = get_circle_area(radius_val)
print(f"Area of circle with radius {radius_val}: {area_val:.2f}")

print("\n--- Returning Multiple Values (as a tuple) ---")
def get_user_info():
    """Gets user input and returns name and age."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age # Returns as a tuple

# name_from_func, age_from_func = get_user_info()
# print(f"User: {name_from_func}, Age: {age_from_func}")

print("\n--- Variable Scope: Local vs. Global ---")
global_message = "I am a global message." # Global variable

def show_scope_example():
    local_message = "I am a local message." # Local variable
    print(f"Inside function (local): {local_message}")
    print(f"Inside function (global): {global_message}")

show_scope_example()
print(f"Outside function (global): {global_message}")
# print(local_message) # This would cause a NameError

# Modifying global variable (use with caution!)
global_counter = 0
def increment_global_counter():
    global global_counter # Declare intent to modify global variable
    global_counter += 1
    print(f"Global counter inside func: {global_counter}")

increment_global_counter()
increment_global_counter()
print(f"Global counter outside func: {global_counter}")
