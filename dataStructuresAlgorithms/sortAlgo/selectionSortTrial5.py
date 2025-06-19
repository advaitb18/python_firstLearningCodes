# selection sort in - place method all in one no formation of new array just swap



array25 = [99,11,21,9,89,77,15,1,98]
n = len(array25)

for i in range(n):
    minElementIndex = i
    for j in range(i+1, n):
        if array25[j] < array25[minElementIndex]:

            minElementIndex = j

    array25[i], array25[minElementIndex] = array25[minElementIndex], array25[i]
    print(f"This is selection sorted: {array25}")


array26 = [99,11,21,9,89,77,15,1,98]
n1 = len(array26)
for i in range(n1):
    maxElementIndex = i
    for j in range(i+1, n1):
        if array26[j] > array26[maxElementIndex]:
            maxElementIndex = j
            print(array26)
    array26[i], array26[maxElementIndex] = array26[maxElementIndex], array26[i]
    print(f"This is selection sorted: {array26}")

