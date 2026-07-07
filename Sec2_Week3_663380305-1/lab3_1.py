def Multiplication_Table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

def Full_Multiplication_Grid():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i*j:4d}", end="")
        print()

def main():
    n = int(input("Enter a number to print its multiplication table: "))
    Multiplication_Table(n)
    print("\nFull Multiplication Grid:")
    Full_Multiplication_Grid()

main()