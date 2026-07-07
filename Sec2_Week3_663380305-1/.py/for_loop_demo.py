print("--- Using for loop with range() ---")
# Loop 5 times (0 to 4)
for i in range(5):
    print(f"Iteration {i}")

print("\n--- Counting from 1 to 10 ---")
for num in range(1, 11): # Start at 1, go up to (but not including) 11
    print(num)

print("\n--- Counting by 2s from 0 to 10 ---")
for even_num in range(0, 11, 2): # Start 0, end 11 (exclusive), step 2
    print(even_num)

print("\n--- Iterating over a string ---")
my_string = "Python"
for char in my_string:
    print(f"Character: {char}")

print("\n--- Calculating sum of first 5 numbers ---")
total_sum = 0
for i in range(1, 6): # Numbers 1, 2, 3, 4, 5
    total_sum += i # Equivalent to total_sum = total_sum + i
print(f"Sum of first 5 numbers: {total_sum}")