# --- Integers ---
age = 30
print("My age is:", age)
print("Type of age:", type(age)) # type() function tells you the data type

# --- Floats ---
price = 19.99
print("The price is:", price)
print("Type of price:", type(price))

# --- Strings ---
name = "Alice"
greeting = 'Hello' # Single quotes also work for strings
message = "Python is fun!"

print(greeting + ", " + name + "!") # String concatenation
print(message)
print("Type of name:", type(name))

# Multi-line string (docstring example, can also be used for multi-line comments)
long_text = """
This is a multi-line string.
It can span across several lines.
Useful for longer descriptions.
"""
print(long_text)

# --- Booleans ---
is_student = True
is_adult = False
print("Am I a student?", is_student)
print("Type of is_student:", type(is_student))
