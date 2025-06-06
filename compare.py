x = int(input("What is x?: "))
y = int(input("What is y?: "))

a = int(input("What is a?: "))
b = int(input("What is b?: "))



if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

if a < b or a > b:
    print("a is not equal to b")
else:
    print("a is equal to b")

if a != b:
    print("a is not equal to b")
if a == b:
    print("a is equal to b")



if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


if a < b or a > b:
    print("a is not equal to b")
else:
    print("a is equal to b")


## below we are using and option as we did with or above

score = int(input("What is score?: "))
if score >= 90 and score <= 100:
    print("you graded A")
elif score >= 80 and score <= 89:
    print("you graded B")
elif score >= 70 and score <= 79:
    print("you graded C")
elif score >= 60 and score <= 69:
    print("you graded D")
else:
    print("you failed")

## if score >= 90 and score <= 100:
## if 90 <= score and score <= 100
## becomes
## if 90 <= score <= 100
if 90 <= score <= 100:
    print("you graded A")
elif 80 <= score <= 89:
    print("you graded B")
elif 70 <= score <= 79:
    print("you graded C")
elif 60 <= score <= 69:
    print("you graded D")
else:
    print("you failed")


## it can become more clever like this below

if score >= 90:
    print("you graded A")
elif score >= 80:
    print("you graded B")
elif score >= 70:
    print("you graded C")
elif score >= 60:
    print("you graded D")
else:
    print("you failed")