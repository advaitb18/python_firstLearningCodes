def main():
    x = int(input("Enter a number x: "))
    y = int(input("Enter a number y: "))
    z = int(input("Enter a number z: "))


    print("x squared is", square(x))
    print("y squared is", square2(y))
    print("z squared is", square3(z))

def square(n):
    return n * n
def square2(n):
    return n ** 2
def square3(n):
    return pow(n, 2)

main()

