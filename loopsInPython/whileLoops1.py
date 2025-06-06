# while lops harvard Python david malan

while True:
    n = int(input("Whats in n?"))
    if n < 0:
        continue
    else:
        break

if n > 0:
    for i in range(n):
        print(i,"MEOWW")



# or other way
print(" same thing other way, until user doesnt input positive number")
while True:
    n = int(input("Whats in n?"))
    if n >0:
        break

for _ in range(n):
    print(_,"bhoWW")



def main():
    moowww(3)

def moowww(n):
    for i in range(n):
        print(i,"->mooWWW")


main()