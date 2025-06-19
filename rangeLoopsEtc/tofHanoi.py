#tower of hanoi trial

def tower_of_hanoi(n,s,h,d):
    if n == 1:
        print(f"This is the {n} from {d}")
        return

    tower_of_hanoi(n-1,s,h,d)
    #print(f"This is the {n-1} from {d}")
    print(f"This is the {n} from {d}")
    tower_of_hanoi(n-1,h,s,d)
   # print(f"This is the {n-1} from {h-1}")
    print(f"This is the {h} TO {s}")


def main():
    n = int(input("Enter the desired target: "))
    tower_of_hanoi(n,0,1,0)
    tower_of_hanoi(n,0,1,1)
    tower_of_hanoi(n,0,1,2)

main()