import sys
from _ast import arguments

print(sys.version)
print(sys.executable)

#try:
#   print("hello my name is",sys.argv[1])
#except IndexError:
#   print("hello my name is",sys.argv[1])

# run code in terminal==> python sysTrial1.py Krishna
# output if you used arguement correctly otherwise there will be IndexError as above but python

print("hello your name is",sys.argv[1])


if len(sys.argv)<2:
    print("too few arguments")
elif len(sys.argv)>2:
   print("too many arguments")

print("hello your age is",sys.argv[1])


for arg in sys.argv:
    print("Hello my args in this arg is:",arg)
#Below we added [1:] it will exclude the first sysTrial1.py in command line argument.
for arg in sys.argv[1:]:
    print("Hello my args in this arg is:",arg)