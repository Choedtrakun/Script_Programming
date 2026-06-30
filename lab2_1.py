def main():
    num = input("Enter a number: ")
    check_number(num)

def check_number(num):
    try:
        num = float(num)
        if num > 0:
            x = "positive"
        elif num < 0:
            x = "negative"
        else:
            x = "zero"

        if num % 2 == 0:
            y = "even"
        else:   
            y = "odd"
        
        print(f"The number is {x} and {y}.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")      

main()