# selection sort final

# ==> Approach 1: make function to find smallest index, now create new function to actually to do selection sort, now pass the array in the smallestIndex function and the smallest index you find pop it in the new array.

def smallestIndex(array):
    smallest = array[0]
    smallestIndex = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallestIndex = i
    return smallestIndex


def selectionSort(array):

    #new array to store the popped elements at the smallestIndex
    newSort = []
    # here we created smallestIndexinSelectionSort variable to store the smallest index we find in array.
    # but do it for all the elements so have to run one loop
    for i in range(len(array)):
        smallestIndexinSelectionSort = smallestIndex(array)
        newSort.append(array.pop(smallestIndexinSelectionSort))
    print(newSort)

def main():
    array = [99,90,89,80,79,70,5,1,45,40,2,0,100]
    selectionSort(array)

if __name__ == "__main__":
    main()