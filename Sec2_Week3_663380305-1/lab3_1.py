def Multiplication_Table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

def main():
    number = int(input("Enter a number to generate its multiplication table: "))
    Multiplication_Table(number)

if __name__ == "__main__":
    main()