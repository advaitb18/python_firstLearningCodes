#Bubble sort algo down - in bubble sort larger number is sorted towards the end first===> 1 outer and 1 inner loop and if left index is smaller than right swap number [small,large] = [large,small] this will be inside inner loop

numsForBubble = []
sizeForBubble = int(input("Enter the size of the bubble array: "))

for i in range(sizeForBubble):
    numsForBubble.append(int(input(f"Enter the number to be bubble sorted{i}: ")))

swapCounter = 0

for j in range(sizeForBubble-1):
    swapped = False
    for i in range(sizeForBubble-1 - j):
        if numsForBubble[i] > numsForBubble[i+1]:
            numsForBubble[i+1], numsForBubble[i] = numsForBubble[i], numsForBubble[i+1]
            swapped = True
            swapCounter += 1

    if not swapped:
        break

print(f"The bubble sorted array is: {numsForBubble}")
print(f"The bubble sorted array counter is:{swapCounter}")