#selection sort with 2nd approach by creating one function for smallest index and copying the smallest index elements to new array

#this function finds the smallestIndex si.

# smallest index for array

# recursive function in which if smallest index out that in new array

# main function to pass array in recursive function


#1. smallestIndex function

def small_index(array):
    smallest = array[0] #value
    smallestIndex = 0   #index

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i] #value
            smallestIndex = i #index

    return smallestIndex

def large_index(array):
    n = len(array)
    largest = array[n-1]
    largestIndex = n-1

    for i in range(n):
        if array[i] > largest:
            largest = array[i]
            largestIndex = i

    return largestIndex


def selSort(array):
    newArray = []
    for i in range(len(array)):
        smallest = small_index(array)
        newArray.append(array.pop(smallest))
        print(newArray)

def selSortM(array):
    newArrayM = []
    for i in range(len(array)):
        largest = large_index(array)
        newArrayM.append(array.pop(largest))
        print(newArrayM)


def main():
    array23 = [151, 21, 34, 49, 245, 66, 79, 85, 1]

    selSort(array23)
    #selSortM(array23)

    array24 = [99,11,21,9,89,77,15,1,98]
    selSortM(array24)

main()