#binary search ==> focus on the mid-counter, basically mid counter is checked for target until divided by 2 and answer is found.it is iterated to find the target basically singe pointer approach

numsBinary = [10,20,45,15,45,12,13,78,45,99,1,2,3,5,7,77]

sortedNumsBinary = sorted(numsBinary)
print(sortedNumsBinary)


targetBinary = int(input("Enter the target number: "))

# left = 0
# right = len(numsBinary) - 1
# Found = False
#
# mid = left + (right-left)//2
# for num in numsBinary:
#     if num == targetBinary:
#         print(f"Target number is found:,{num} ")
#         Found = True
#         break
#     elif num < targetBinary:
#         left = mid + 1
#     elif num > targetBinary:
#             right = mid - 1
#
# if not Found:
#     print("Number not found")

numsBinary2 = sorted(numsBinary)

left2 = 0
right2 = len(numsBinary2) - 1
Found2 = False

while left2 <= right2:
    mid = (left2 + right2) // 2
    if numsBinary2[mid] == targetBinary:
        print(f"Target number is found,{numsBinary2[mid]} ")
        Found2 = True
        break
    elif numsBinary2[mid] < targetBinary:
        left2 = mid + 1
    else:
        right2 = mid - 1

if not Found2:
    print("Number not found")