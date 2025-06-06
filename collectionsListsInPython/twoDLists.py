#twoDLists.py


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]  #this is at groceries[0]
vegetables = ["carrot", "cucumber", "pepper", "tomato", "potato"] #this is at groceries[1]
vitaminMinerals = ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin E"] #this is at groceries[3]

groceryList = [fruits, vegetables, vitaminMinerals]
print(groceryList)
print(groceryList[0][0])
print(groceryList[0][1])
print(groceryList[0][2])
print(groceryList[0][3])
print(groceryList[0][4])
print("")
print(groceryList[1][0])
print(groceryList[1][1])
print(groceryList[1][2])
print(groceryList[1][3])
print(groceryList[1][4])
print("")
print(groceryList[2][0])
print(groceryList[2][1])
print(groceryList[2][2])
print(groceryList[2][3])


print("")

print(groceryList[1][1:3])

print("")


groceryList2 = [    ["apple", "banana", "cherry", "kiwi", "mango"],
                    ["carrot", "cucumber", "pepper", "tomato", "potato"],
                    ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin E"] ]

for collection in groceryList2:
    print(collection)
    for item in collection:
        print(item)




