def hello(to: object = "world") -> None:
    print(f"Hello, {to}!")

hello()
name = input("Enter your name: ")
hello(name)
hello(to="everyone")
hello(to="coders")


age = str(input("Enter your age: "))
hello(age)
hello(to=age)
hello(to="Coders of all age, you are all welcome")




