# remiander style still needs to learn

year = int(input("Enter year: "))
def is_leap(year):
    if not year % 4:
        leap = True
        if not year % 100 and year % 400:
            leap = False
        return leap

def main():
    print(is_leap(year))

main()