# quicksort trial
import random
from array import array
from random import choice


def quickSort2(array):
    #base case
    if len(array) <= 1:
        return array
    else:
        pivotIndex = array[0]
        lessThanPivotIndex = [i for i in array [1:] if i <= pivotIndex]
        greaterThanPivotIndex = [i for i in array [1:] if i >= pivotIndex]

        return quickSort2(lessThanPivotIndex) + [pivotIndex] + quickSort2(greaterThanPivotIndex)


def main():
 #array = [random.choice(range(100))]
    array= [15,1,9,24,58,47,99,2,3,89]
    a=(quickSort2(array))
    print(a)

if __name__ == "__main__":
    main()

