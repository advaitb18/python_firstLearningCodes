
name = input("Enter your name: ")

age = int(input("Enter your age: "))

while name == "":
    name = input("Enter your name: ")
    print("Your name is: ", name)

print(f"Your name is: {name}")



while age <= 0:
    print("Your age can't be negative")
    age = int(input("Enter your age: "))

print(f"Your age is: {age}")
