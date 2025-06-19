#find Smallest Number in Array
# Selection sort takes 1 function and pass array in that function
#


def main():
    #findSmallest([9,8,5,1,99,999,2,5,7,6])
    findSmallestInArray = []
    sizeForFindSmallest = int(input("Enter the size of the find smallest array: "))
    for _ in range (sizeForFindSmallest):
        findSmallestInArray.append(int(input("Enter the size of the quick sort array: ")))

    print (findSmallestInArray)
    findSmallest(findSmallestInArray)


def findSmallest(arraY):
    smallest = arraY[0]
    smallestIndex = 0

    for i in range(1, len(arraY)):
        if arraY[i] < smallest:
            smallest = arraY[i]
            smallestIndex = i


    print(f"The smallest element is: {smallest} at index: {smallestIndex}")



main()