print("--- Simple while loop (countdown) ---")
count = 5
while count > 0:
    print(f"Count: {count}")
    count -= 1 # Decrement count (important to avoid infinite loop)
print("Countdown finished!")

print("\n--- Input validation with while loop ---")
user_input = ""
while not (user_input == "yes" or user_input == "no"):
    user_input = input("Please enter 'yes' or 'no': ").lower()
print(f"You entered: {user_input}")

print("\n--- Using 'break' to exit early ---")
secret_number = 7
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    guess_str = input(f"Guess the number (1-10) - Attempt {attempts + 1}/{max_attempts}: ")
    guess = int(guess_str)
    attempts += 1
    if guess == secret_number:
        print("Congratulations! You guessed it!")
        break # Exit loop immediately if correct
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else: # This 'else' block runs if the loop completes *without* a break
    print(f"Sorry, you ran out of attempts. The secret number was {secret_number}.")

print("\n--- Using 'continue' to skip iterations ---")
for i in range(1, 11): # Numbers 1 to 10
    if i % 2 != 0: # If number is odd, skip the print
        continue # Go to the next iteration
    print(f"Even number: {i}") # Only even numbers will be printed
