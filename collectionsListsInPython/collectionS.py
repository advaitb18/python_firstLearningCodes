# collection = single "variable" used to store multiple values
    #List = [] ORDERED AND CHANGEABLE. Duplicates OK.
    #Set = {} UNORDERED and IMMUTABLE. No duplicates. But add/remove OK.
    #Tuple = () ORDERED and UNCHANGEABLE. Duplicates are NOT OK. FASTER. Use tuple over List, or even when you don't need to change the values.

fruits = ["apple", "banana", "cherry"]

print(fruits[0] + fruits[1] + fruits[2])
print(fruits)
print(fruits[:2])
print(fruits[::2])
print(fruits[::-2])
print(fruits[2:])

for fruit in fruits:
    print(fruit)



vegetables = ["brocolli", "mushrooms" , "asparagus"]


#dir gives the methods and attributes this collection can perform you can use help function print(help(fruits)) to show full list description.
print(dir(fruits))
print(dir(vegetables))


print(len(fruits))


# check as a boolean
print("apple" in fruits)

# assign through index

fruits[1] = "pineapple"
fruits[2] = "orange"

fruits.append("grapes")
fruits.insert(5, "watermelon")
#fruits.remove("cherry")
fruits.sort()
fruits.reverse()

print(fruits.index("orange"))
print(fruits.count("apple"))





# Set

vitamins = {"Vitamin A", "Vitamin C", "Vitamin D"}

#print(dir(vitamins))
#print(help(vitamins))

vitamins.add("Vitamin B12")
vitamins.add("Vitamin C12")
vitamins.remove("Vitamin C12")

print(vitamins)

print(fruits)





# Tuple () Ordered and unchangeable. Duplicates OK. FASTER

commodities = ("Gold", "Silver", "Bronze")

#print(dir(commodities))
#print(help(commodities))
print(len(commodities))

print(commodities[0])
print(commodities[1])
print(commodities[2])

print("Gold"in commodities)
