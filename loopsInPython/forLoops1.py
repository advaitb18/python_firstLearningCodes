#for loops python by harvard - david malan

for x in range(0,20):
    print(x)

for x in range(100,200):
    if x == 177:
        break
    print(x)

for i in [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]:
    print(i,end=" ")
print()


for x in range(0,2):
    print("you can add anything directly but you dont have to worry about i variable , this is really called PYTHONIC")


# what is more pythonic

print("Look, here you can directly print something without even giving range but just multiply\n" * 4, end="")
