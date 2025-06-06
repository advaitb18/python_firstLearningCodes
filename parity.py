## code parity



x = int(input("enter a number: "))
if x % 2 == 0:
    print("even")
else:
    print("odd")



def main ():
    x = int(input("enter a number: "))
    if is_even(x):
        print("even")
    else:
        print("odd")


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_odd(x):
    return True if x % 2 == 1 else False

def is_Even(x):
    return x % 2 == 0
print(is_Even(x))

main()