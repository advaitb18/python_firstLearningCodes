# here I will be testing different code to learnt hte effects
from typing import Any

array = [15,1,9,24,58,47,99,2,3,89]
length = len(array)


# Pattern printing
for i in range(1):
    print("$" * 3)
print("Above code will print $ three times in col - 1 time in row")


for i in range(2):
    print("$" * 3)
print("Above code will print $ three times col - 2 times in row")

#we can do this as well
for row in range(2):
    print("$" * 3)
    for col in range(2):
        print("#" * 3)
print("Here the first loop will run and print $ three times in col and then run inner loop which will run two times in row and "
      "print # three times in col twice and then again outer loop for one more time doing exactly same steps what was done initially")

for i in range(1):
    print("$" * 3)
    for j in range(1):
        print("#" * 3)
print("blank line")

array2 = [100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
print(array2[1:])
print(array2[2:])
print(array2[3:])
print(array2[4:])
print(array2[5:])
print(array2[6:])
print(array2[7:])
print(array2[8:])
print("blank line :")
print(array2[:1])
print(array2[:2])
print(array2[:3])
print(array2[:4])
print(array2[:5])
print(array2[:6])
print(array2[:7])
print(array2[:8])
print(" ")
print("Blank Line: Below we are printing negative value like -1:, -2:")
print(array2[-1:])
print(array2[-2:])
print(array2[-3:])
print(array2[-4:])
print(array2[-5:])
print(array2[-6:])
print(array2[-7:])
print(array2[-8:])

print("Blank Line: Below we are printing negative value like :-1, :-2")
print(array2[:-1])
print(array2[:-1])
print(array2[:-2])
print(array2[:-3])
print(array2[:-4])
print(array2[:-5])
print(array2[:-6])
print(array2[:-7])
print(array2[:-8])



print(" ")
midArray2n = (len(array2) // 2)
print(f"{(array2[:midArray2n])} and {(array2[midArray2n:])}")

for i in range(midArray2n):
    print(array2[i], end="$")

print("This is i in range of midarray2n which is half of the length of array2, for that number it will print the values of array2[i]")

for i in range(len(array2)):
    print(array2[i], end="$")

