import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
# in the output function is still called from the imported package sayings thats why it is useful to use---> if: __name__ == "__main__"