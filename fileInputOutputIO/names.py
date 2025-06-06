
#empty list
names = []
for _ in range(3):
    # input("What is your name?")
    # names.append(names)
    names.append(input("Enter a name: "))

for name in sorted(names):
    print(f"hello,{name}")


name = input("Enter a name: ")
print(f"name is, {name}")


# open is opening a file and allows us to write when we pass open("names.txt","w") or ,"r" for read, or "a" for append. Also you will see names.txt created in project structure

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()

# more pythonic way to manipulate files in python also you don't have .close

links = input("Enter links: ")
with open("links.txt","a") as enterLinks:
    enterLinks.write(f"{links}\n")

## here is the way to read from the file we can use examples of names and links
with open("names.txt","r") as file:
    linesFromFile = file.readlines()

for line in linesFromFile:
    print("hello,",line.rstrip())
    print(f"hello, {line}")


with open("links.txt","r") as enterLinks:
    for link in enterLinks.readlines():
        print("Hello",link.rstrip())