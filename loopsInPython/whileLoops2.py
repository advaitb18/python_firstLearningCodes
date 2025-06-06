def main():
    number = get_number()
    hariom(number)

def get_number():
    while True:
        n = int(input("Enter a n: "))
        if n > 0:
            break
    return n

def hariom(n):
    for i in range(n):
        print(i,"Hari:Om")


main()