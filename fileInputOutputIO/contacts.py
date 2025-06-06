# import csv
#
# contacts = []
#
# # for _ in range(2):
# #     contacts.append(input("Enter a name: "))
#
# file = open("contacts.txt", "a")
# file.write("\n".join(contacts))
# file.close()
#
# # more pythonic way
#
# contacts = input("Enter contacts separated by comma: ")
# with open("contacts.txt", "a") as file:
#     file.write(f"{contacts}\n")
#
# with open("contacts.txt", "r") as file:
#     contactsFromFile = file.readlines()
#     for contact in contactsFromFile:
#         print("This is your contact::",contact.rstrip())
#
# with open("contacts.txt", "r") as file:
#     reader = csv.reader(file, delimiter=",", quotechar='"')
#     for row in reader:
#         print(row)
#
# with open("contacts.txt", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         contacts.append({"name": row["name"], "number": row["number"]})
#
# for contact in sorted(contacts, key=lambda contact: contact["name"]["number"]):
#     print(f"Hello,{contact['name']} is from {contact['number']}")