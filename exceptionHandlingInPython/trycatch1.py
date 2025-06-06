try:
    a = int(input("What is a? "))
except ValueError:
    print("Please enter a integer number only.")

print(f"The value of a is: {a} ")


try:
    b = int(input("What is b? "))
except ValueError:
    print("Please enter a integer number only.")
else:
    print(f"The value of b is: {b} ")



while True:
    try:
        c = int(input("What is c? "))
    except ValueError:
        print("Please enter a integer number only.")
    else:
        #print(f"The value of a is: {c} ")
        #if you use print here it will go on never end loop, that's why use break here nad print below
        break

print(f"The value of c is: {c} ")

def main():
    f = get_float()
    print(f"The value of f is: {f} ")

    i = get_intPythonic()
    print(f"The value of i is: {i} ")


def get_float():
    while True:
        try:
            f = float(input("What is f? "))
        except ValueError:
            print("Please enter a float number only.")
        else:
            return f

def get_intPythonic():
    while True:
        try:
            return int(input("What is i? "))
        except ValueError:
            pass


main()