def main():
    num = input("Enter your age: ")
    x = check_number(num)
    # print(f"Your age is {num}. {type(x)}")
    if type(x) == int:
        like_action_movies(num)

def check_number(num):
    try:
        num = int(num)
        if num < 0:
            x = "Bro wasn't even born yet!"
        elif num < 5:
            x = "You're too young for movies! Enjoy cartoons."
        elif num < 12:
            x = 'Recommend "G-rated or PG-rated movies."'
        elif num < 17:
            x = 'Recommend "PG-13 or R-rated (with parentalguidance)."'
        else:
            x = 'Recommend "Any movie rating."'
        print(f"Your age is {num}. {x}")
    except ValueError:
        print("Invalid input. Please enter your age.")
    
    return num


def like_action_movies(x):
    try:
        action_movies = input("Do you like action movies? (yes/no): ")
        # print(f"{x} {type(x)}")
        if action_movies == "yes" and int(x) >= 18:
            print("You might enjoy the latest action blockbuster!")
        elif action_movies == "no" and int(x) >= 18:
            print("I suggest your porn.")
    except ValueError:
        print("Invalid input. Please enter 'yes' or 'no'.")

main()