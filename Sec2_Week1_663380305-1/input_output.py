# input_output.py

# --- Basic Output ---
print("This is a simple message.")
print("Python is fun!", end=" ") # 'end' parameter
print("Let's learn together.")
print("Item 1", "Item 2", "Item 3", sep=" | ") # 'sep' parameter

# --- Basic Input ---
# Get user's name
name = input("Please enter your name: ")
print(f"Hello, {name}!")

# Get user's age (input() returns a string!)
age_str = input("What is your age? ")
print(f"You entered: {age_str} (Type: {type(age_str)})")

# Convert age to an integer for calculations
age_int = int(age_str)
next_year_age = age_int + 1
print(f"Next year, you will be {next_year_age} years old.")

# Get a decimal number and convert to float
price_str = input("Enter a price (e.g., 19.99): ")
price_float = float(price_str)
tax = price_float * 0.07
total_price = price_float + tax
print(f"Original price: ${price_float:.2f}") # Format to 2 decimal places
print(f"Tax (7%): ${tax:.2f}")
print(f"Total price: ${total_price:.2f}")
