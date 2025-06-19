# two-pointer approach ===> take 2 pointers one at 0th and one at last index, run the loop if sum is larger than target, decrement the right index and if sum is larger than target, increment the left index

nums2Pointer = []
s = (int(input("size of array for 2 pointers approach: ")))

for i in range(s):
    nums2Pointer.append(int(input("Enter number for 2 pointer approach: ")))

print(nums2Pointer)

print(sorted(nums2Pointer))

## two numbers addition is equal to target

left3 = 0
right3 = len(nums2Pointer) - 1
targetfor2NumbersAddition = int(input("Enter target for 2 numbers addition: "))
#found3 = False

while left3 < right3:
    if nums2Pointer[left3] + nums2Pointer[right3] == targetfor2NumbersAddition:
        print(f"Number found {nums2Pointer[left3]} plus {nums2Pointer[right3]} equals to {targetfor2NumbersAddition} ")
        break
        #found3 = True
    elif nums2Pointer[left3] + nums2Pointer[right3] > targetfor2NumbersAddition:
        nums2Pointer[right3] -= 1
    else:
        nums2Pointer[left3] += 1

#if not found3:
 #   print("Number not found")