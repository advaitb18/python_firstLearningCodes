#Selection sort ==> Selection sort is a neat algorithm, but it’s not very fast.
#       Quicksort is a faster sorting algorithm that only takes O(n log n) time. It’s coming up in the next chapter!

numsForSelectionSort = []
sizeForSelectionSort = int(input("Enter the size of the selection sort array: "))

for i in range(sizeForSelectionSort):
    numsForSelectionSort.append(int(input("Enter the element to be inserted: ")))

#code here
def findSmallest(numsForSelectionSort):
    smallest = numsForSelectionSort[0]
    smallestIndex = 0

    for i in range(1, len(numsForSelectionSort)):
        if numsForSelectionSort[i] < smallest:
            smallest = numsForSelectionSort[i]
            smallestIndex = i
    return smallestIndex



def selectionSort(numsForSelectionSort):
    newNumsForSelectionSort = []
    for i in range(len(numsForSelectionSort)):
        smallestIndex1 = findSmallest(numsForSelectionSort)
        newNumsForSelectionSort.append(numsForSelectionSort.pop(smallestIndex1))
    print(newNumsForSelectionSort)

def main():
    selectionSort(numsForSelectionSort)


if __name__ == '__main__':
    main()
