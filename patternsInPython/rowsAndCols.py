def print_square(size):
    # For each row in square
    for i in range(size):

        #For each cols in square
        for j in range(size):
            print(".", end="")
        print(" ")

def print_squarePythonic(size):

    for i in range(size):
        print("$" * size)
    print(" ")



def main():
    print_square(4)
    print_squarePythonic(8)

main()