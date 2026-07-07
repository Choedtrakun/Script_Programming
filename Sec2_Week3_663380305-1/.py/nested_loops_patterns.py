print("--- Printing a 5x5 square of asterisks ---")
size = 5
for row in range(size):
    for col in range(size):
        print("* ", end="") # Print asterisk and space, don't go to new line
    print() # Go to the next line after each row is complete

print("\n--- Printing a right-angled triangle ---")
height = 5
for row in range(1, height + 1): # For each row (1 to 5)
    for col in range(row): # Print 'row' number of asterisks
        print("* ", end="")
    print()

print("\n--- Printing an inverted right-angled triangle ---")
for row in range(height, 0, -1): # From 5 down to 1
    for col in range(row):
        print("* ", end="")
    print()
