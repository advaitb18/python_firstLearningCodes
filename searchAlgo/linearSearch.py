nums = (45,99,88,11,558,147,279,369,1,2,3,4)
target = int(input("Enter number to linear search:"))

found = False
# for num in nums:
#     if num == target:
#         print("Number found")
#         found = True
#         break
# if not found:
#         print("Number not found")
#
# for target in nums:
#     if target == target:
#         print("Number found")
#         break
#     else:
#         print("Number not found")

for num in nums:
    if num == target:
        print(f"Number found at index:  {num}")
        found = True
        break

if not found:
        print("Number not found")

