#List===> locations that are numeric ==> print(students[0])
students = ["1Hermione","Harry","Malfoy"]
print(students)
print(len(students))
print(students[0])
print(students[1])
print(students[2])

print(students[0],students[1],students[2],end=" ")

for student in students:
    print(student)

for i in range(len(students)):
    print(i, students[i])

for i in range(len(students)):
    print(i + 1, students[i])


#

houses = ["Gryffindor","Gryffindor","Slytherin"]

# dictionaries ==> allows you to use actual words for the indices or your indexes like: print(students["Hermione"]

students1 = {
    # KEY     :   VALUE
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Malfoy" : "Slytherin"
}
#print(students[0]==> in list
print(students1["Hermione"])

print("student is KEY")
print("students1 is value")

for student in students1:
    print(students1)
    print(students,students1)
    print(students1[student])

print("Below are new values:::::::::::::::::::::::::::::::::::::::::::")




#
#None is a special keyword in python None is literally none like there is no patronus for malfoy in Harry Potter
students2 = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus"  : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus"  : "Stag"},
    {"name" : "Malfoy", "house" : "Slytherin", "patronus"  : "None"}
]

print(students2)
print("123123123")

print("names from students2")
for student in students2:
    print(student["name"])


print("Names, Houses  and Patronus from students2 all together")
for student in students2:
    print(student["house"],student["name"],student["patronus"], sep=" ==:> ")
