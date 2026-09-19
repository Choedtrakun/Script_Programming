# lab6_1.py

def add(a, b):
    """Add two numbers together."""
    return a + b


def subtract(a, b):
    """Subtract the second number from the first number."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide the first number by the second number."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def power(base, exponent=2):
    """Return the base number raised to an exponent."""
    return base ** exponent


def calculator():
    """Run the calculator menu."""
    while True:
        print("\n===== Calculator =====")
        print("1 - Addition")
        print("2 - Subtraction")
        print("3 - Multiplication")
        print("4 - Division")
        print("5 - Power (Challenge)")
        print("0 - Exit")

        option = input("Select an option: ")

        if option == "0":
            print("Program ended.")
            break

        if option == "5":
            try:
                base = float(input("Enter base: "))
                exponent = input("Enter exponent (press Enter for 2): ")

                if exponent == "":
                    answer = power(base)
                else:
                    answer = power(base, float(exponent))

                print("Answer:", answer)

            except ValueError:
                print("Please enter a valid number.")

            continue

        if option not in ("1", "2", "3", "4"):
            print("Invalid option.")
            continue

        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number. Try again.")
            continue

        if option == "1":
            result = add(first, second)
        elif option == "2":
            result = subtract(first, second)
        elif option == "3":
            result = multiply(first, second)
        else:
            result = divide(first, second)

        print("Answer:", result)


if __name__ == "__main__":
    calculator()