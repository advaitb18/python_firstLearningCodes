import re
from _ast import pattern

email = input("What is your email").strip()
if "@" in email and "." in email:
    print("This email is valid and registered.")
else:
    print("This email is not valid.")

username , domain = email.split("@")
if username and domain.endswith(".edu") and "." in domain:
    print("This email is valid and can be registered.")
else:
    print("This email is not valid.")

# to improve this we can use Regular Expressions (RegEx) --> here the library is re

# re.search(pattern, string, flags=0)

emailAddress = input("What is your EMAIL-ADDRESS?").strip()

if re.search("@", emailAddress):
    print("This email is valid and again can be registered.")
else:
    print("This email is not valid.")

# make note of the following:
# . = any character except a newline
# * = 0 or more repetitions
# + = 1 or more repetitions
# ? = 0 or 1 repetition
# {m} = m repetitions
# {m,n} = m to n repetitions


if re.search(".*@.*", emailAddress):
    print("This email is valid and again can be registered!1")
else:
    print("This email is not valid.")

if re.search(".+@.+", emailAddress):
    print("This email is valid and again can be registered!!!!2")
else:
    print("This email is not valid.")

if re.search("..*@..*", emailAddress):
    print("This email is valid and again can be registered!!!!3")
else:
    print("This email is not valid.")