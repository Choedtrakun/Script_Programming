import time

def Blast_off(n):
    while True:
        print(n)
        n -= 1
        time.sleep(1)
        if n < 0:
            print("Blast off!")
            break

Blast_off(10)