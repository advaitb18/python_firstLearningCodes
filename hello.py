from http.client import responses

print("Hello World!")

def hello(fname,lname):
    print("Hello World! "+fname+" "+lname+"")

hello("HARI","OM")

a,b,c=1,2,3
a,b,c = c,b,a
print(a,b,c)


#Variables = string, integer, float, boolean

f_name = "HARI"
l_name = "OM"
age = 20
is_male = True

print(f_name+" "+l_name+" is "+str(age)+" years old.")


#exercise

length = input("Enter the length of the rectangle: ")
width = float(input("Enter the width of the rectangle: "))

area = int(length) * (width)

print(f'the area is: {round(area,5)} cm²')


response = input("Do you want to continue? (Y/N): ")

if response == "Y":
    print("Okay, let's continue.")
elif response == "N":
    print("Okay, bye.")
else:
    print("Invalid input.")



is_online = input("Do you want to sell this item? (yes/no): ")
if is_online == "yes":
    print("Okay, let's sell it.")
elif is_online == "no":
    print("Okay, bye.")




# Operators (+ , - , * , /)

#Most consistent way to make calculator
Operator_Chosen = input("Enter the Operator (+,-,/,*): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if Operator_Chosen == "+":
    result = num1 + num2
    print(round(result,9))
elif Operator_Chosen == "-":
    result = num1 - num2
    print(round(result,9))
elif Operator_Chosen == "*":
    result = num1 * num2
    print(round(result,9))
elif Operator_Chosen == "/":
    result = num1 / num2
    print(round(result,9))
else:
    print("Invalid input.")


# if else statements in ternary operator way

num_for_ternary = int(input("Enter a number to check Positive/Negative: "))

print("Positive" if num_for_ternary > 0 else "Negative")


num_for_oddEven = int(input("Enter a number to check Odd/Even: "))
print("Even" if num_for_oddEven % 2 == 0 else  "Odd")




# String Indexing = accessing elemetns of a sequence using [] (indexing operator) using this [start:stop:step]


credit_number = "1234-5678-9012-3456"

print(credit_number[0]) ,"", (credit_number[0:4]) ,"", (credit_number[0:4:2]) ,"", (credit_number[::-1]) ,"", (credit_number[::-2])



