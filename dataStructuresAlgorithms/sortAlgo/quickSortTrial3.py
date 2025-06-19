
def quickSort3(array):
    if len(array) < 2:
        return array
    else:
        pivotInd = [6]
        leftPart = [9,5,3]
        rightPart = [4,2,0]

#        pivot = [numbers[pivot_index]]  # Pivot as a single-element list

        return quickSort3(leftPart) + [pivotInd] + quickSort3(rightPart)

def main():


    a = (quickSort3)
    print(a)

if __name__ == '__main__':
    main()
