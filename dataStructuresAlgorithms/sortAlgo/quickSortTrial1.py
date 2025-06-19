# QuickSort is an efficient sorting algorithm that works by selecting a "pivot" element, then rearranging the other elements into two partitions: those less than the pivot and those greater than the pivot. It then recursively sorts each partition. Here’s a step-by-step breakdown:
# - Choose a Pivot: Pick an element in the array (common choices include the first, last, or middle element).
# - Partition the Array: Rearrange elements so that values smaller than the pivot move to the left, and larger values move to the right.
# - Swap Elements: Ensure that the pivot ends up in its correct sorted position.
# - Recursively Sort Partitions: Apply the same process to the left and right partitions until the entire array is sorted.
# - Base Case: If a partition contains one or zero elements, it's already sorted.
# Example:
# Consider the array [8, 4, 7, 3, 9, 1, 5] using QuickSort:
# - Choose 5 as the pivot.
# - Partition: [4, 3, 1] | 5 | [8, 7, 9]
# - Recursively sort [4, 3, 1] → [1, 3, 4]
# - Recursively sort [8, 7, 9] → [7, 8, 9]
# - Final sorted array: [1, 3, 4, 5, 7, 8, 9]
#
# quick sort ===>  QuickSort allows flexibility in selecting the pivot. The choice of pivot affects performance and partitioning efficiency. There isn't a strict convention; it's more about optimizing for different scenarios. Common pivot strategies include:
# - First Element as Pivot – Simple, but can cause poor performance on already sorted arrays.
# - Middle Element as Pivot – Reduces the chance of worst-case performance.
# - Last Element as Pivot – Common choice, simple implementation.
# - Random Element as Pivot – Helps avoid worst-case scenarios.

numsForQuickSort = []
sizeForQuickSort = int(input("Enter the size of the quick sort array: "))

for i in range(sizeForQuickSort):
    numsForQuickSort.append(int(input(f"Enter the element to be inserted:{i} ")))

#code here

minElement = 0

for i in range(sizeForQuickSort):
    if numsForQuickSort[i] < numsForQuickSort[minElement]:
        numsForQuickSort[minElement] = numsForQuickSort[i]
        minElement += 1

print(numsForQuickSort)



