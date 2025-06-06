def main():
    height = int(input("How much height? "))

    print_column(2)
    print_column1(height)
## this is very important : print_column(2) will make run the print_column(height)  will print $ two times
## as by default... but if you see the print_column1(height) and as per user input, it will p rint. equal to user input of height
    width = int(input("How much width? "))
    print_width(width)
    print(" ")
    print_width(10)

def print_column(height):
    for row in range(height):
        print("$\n", end="")


def print_column1(height):
    print(".\n" * height , end="")

def print_width(width):
    for column in range(width):
        print(".", end="")

main()