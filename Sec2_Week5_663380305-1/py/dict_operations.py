print("--- Dictionary Creation and Access ---")

# Creating a dictionary
student_profile = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "gpa": 3.7,
    "courses": ["Python 101", "Data Structures", "Calculus I"]
}

print(f"Student Profile: {student_profile}")

# Accessing values
print(f"Student's Name: {student_profile['name']}")
print(f"Student's Age: {student_profile.get('age')}")  # Using get()
print(
    f"Student's City (using get with default): "
    f"{student_profile.get('city', 'Not Specified')}"
)

# Accessing a non-existent key will raise KeyError if not using .get()
# print(student_profile['city'])  # Uncomment to see error

print("\n--- Adding and Modifying Dictionary Elements ---")

# Adding a new key-value pair
student_profile["city"] = "Bangkok"
print(f"After adding city: {student_profile}")

# Modifying an existing value
student_profile["gpa"] = 3.9
print(f"After updating GPA: {student_profile}")

# Using a variable as a key
favorite_language = "favorite_lang"
student_profile[favorite_language] = "Python"
print(f"After adding favorite language: {student_profile}")

print("\n--- Removing Elements from Dictionary ---")

# Using del
del student_profile["courses"]
print(f"After deleting 'courses': {student_profile}")

# Using pop()
removed_major = student_profile.pop("major")
print(f"Removed major: {removed_major}")
print(f"After popping 'major': {student_profile}")

# Using popitem() (removes last inserted in Python 3.7+)
random_item = student_profile.popitem()
print(f"Removed random item: {random_item}")
print(f"After popitem: {student_profile}")

# student_profile.clear()  # Empties the dictionary
# print(f"After clear: {student_profile}")

print("\n--- Iterating Through Dictionaries ---")

my_book = {
    "title": "The Python Journey",
    "author": "A. Coder",
    "pages": 350,
    "published": 2023
}

print("Iterating over keys:")
for key in my_book:  # Default iteration is over keys
    print(key)

print("\nIterating over values:")
for value in my_book.values():
    print(value)

print("\nIterating over key-value pairs (items):")
for key, value in my_book.items():
    print(f"{key}: {value}")

print("\n--- Checking for key existence ---")
if "author" in my_book:
    print("Author exists in the book dictionary.")