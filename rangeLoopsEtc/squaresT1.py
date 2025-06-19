#square of a number or array
from statistics import median

squares = []

for value in range(1,11):
    square = value**3
    print(f"The square of {value} is this: {square}.")
    squares.append(square)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,10]
a = min(digits)
b = max(digits)
c = sum(digits)
d = median(digits)
print(a ,b ,c)
print(d)


#slicing a list
players = ['Shewag','Ganguly','Rahul','Tendulkar','AKhtar','parthiv']

print(players)
print(players[0:3])
print(players[1:4])
print(players[2:5])
print(players[2:])
print(players[-3:])

for player in players[:4]:
    print(player)

ind_players = players[:-2]
print(ind_players)

