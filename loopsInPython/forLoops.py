
for x in (range(1,10)):
    print(x)

print("Hello")

for x in reversed(range(1,10)):
    print(x)

print("Hello")

step =+ 4
for x in range(1,20, step):
    print(x)



Phone_Number = input("Enter your phone number: ")


for x in Phone_Number:
    print(x)


for x in range(1,20):
    if x == 13:
        break
    else:
        print(x)

for x in range(1,20):
    if x == 13:
        continue
    else:
        print(x)