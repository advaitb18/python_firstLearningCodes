def main():
    name = input("Enter your name: ")
    hello(to=name)

def hello(to):
    print("Hello " + to)
    # name scope is not available in hello function ===> print("Hello,",name)

main()

