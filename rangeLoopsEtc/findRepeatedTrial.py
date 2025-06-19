#find the occurrences in the array

array = [14,28,14,53,2,5,7,14,28]
n = len(array)
desiredTarget = int(input("Enter the desired target: "))
counter = 0
for i in range(n):
    if array[i] == desiredTarget or array[i]/2 == desiredTarget:
        counter += 1
    else:
        counter += 0

print(counter)

