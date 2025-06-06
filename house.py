name = input("Enter your name: ")

if name == "Harry" or name == "Harry" or name == "Henry" or name == "Hermione":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Whos this?")

name2 = input("Enter your name2: ")

match name2:
    case "Modi":
        print("BJP")
    case "Amit Shah" | "Amith Shah Ahmedabad" | "Vijay Rupani" :
        print("BJP")
    case "Rahul GAndhi" | "soniya gandhi" | "Manmohan Singh":
        print("c0ngress")
    case _:
        print("Whos this?")

