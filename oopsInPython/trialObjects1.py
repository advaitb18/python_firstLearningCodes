#trialObjects1.py

class Car:
    def __init__(self, brand, year, model, color):
        self.brand = brand
        self.year = year
        self.model = model
        self.color = color

    def start_engine(self):
        print(f"Engine started for {self.brand} {self.model} of {self.color}")


#Creating Objects

my_sportsCar1 = Car("BMW", 2020, "M3 Series", "Black")
my_sportsCar2 = Car("AUDI", 2022, "RS5 Series", "Red")

my_luxuryCar1 = Car("Rolls-royce", 2022, "Phantom", "White")
my_luxuryCar2 = Car("Lamborghini", 2022, "Urus", "Yellow")


my_sportsCar1.start_engine()
my_sportsCar2.start_engine()
my_luxuryCar1.start_engine()
my_luxuryCar2.start_engine()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Dog is barking")

    breed = "USA"


def bark(self):
    print("Dog is barking")


my_dog1 = Dog("Leo-GSD","2")
my_dog2 = Dog("Meo-Pom","2")

my_dog1.bark()
my_dog2.bark()

print(f"My Dog's profile is: {my_dog1.name}, age is: {my_dog1.age} and mated in: {my_dog1.breed}")
print(f"My Dog's profile is: {my_dog2.name}, age is: {my_dog2.age} and mated in: {my_dog2.breed}")

dogProfileList = [my_dog1, my_dog2]

for dog in dogProfileList:
    for key, value in dog.__dict__.items():
        print(f"{key} : {value}")

print("New idea below to do same thing")

dogProfileList2 = [my_dog1.__dict__, my_dog2.__dict__]

for dog in dogProfileList2:
    for key, value in dog.items():
        print(f"{key} : {value}")

print("One more New idea below to do same thing")

dogProfileList3 = {my_dog1, my_dog2}

for dog in dogProfileList3:
    for key, value in dog.__dict__.items():
        print(f"{key} : {value}")


print("One more New idea below to do same thing")
dogProfileList4 = (my_dog1, my_dog2)

for dog in dogProfileList4:
    for key, value in dog.__dict__.items():
        print(f"{key} : {value}")