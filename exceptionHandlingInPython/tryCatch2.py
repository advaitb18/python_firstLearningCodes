def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
                print("Please enter a number.")
        else:
            return get_int(prompt)




def main():
   # get_int(prompt="Enter a number: ")
   e = get_int(prompt="Enter a number: ")
   print(f" This is value of e: {e}")
   # print(get_int(prompt="Enter a number: "))
main()
