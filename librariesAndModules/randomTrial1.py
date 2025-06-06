import random
from random import choice

b = random.choice(range(10))
a = random.choice(["Heads","Tails","None","Head22","Tails44", "123","456"])
print(a)
print(b)

#By importing choice from random and I don't have to use random.choice repeatedly
coin = choice(["Heads","Tails","None","Head22","Tails44"])
print(coin)

x = random.randint(111,999)
print(x)

cards = ["jack","queen","king","ace"]
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)

