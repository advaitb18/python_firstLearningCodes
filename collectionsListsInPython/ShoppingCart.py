# ShoppingCart.py
#Shopping Cart Program


foods = []
prices = []
total = 0

while True:
    food = input("Enter a food item to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = input(f"Enter the price of {food}: $ ")
        foods.append(food)
        prices.append(float(price))

print("Your shopping cart:")

for i in range(len(foods)):
    print(f'{foods[i]}: ${prices[i]}')
    total += prices[i]
    print(f'Total: ${total}')


for food in foods:
    print(food)
    for price in prices:
        print(price)