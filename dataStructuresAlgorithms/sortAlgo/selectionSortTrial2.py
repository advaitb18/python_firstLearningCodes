 #selecction sort

arraySel1 = [99,12,45,1,2,5,9,7,15,12,3,241,45]
n = len(arraySel1)


def selectSort(arraySel1):
 for i in range(n):
     minI = i
     for j in range(i+1, len(arraySel1)):
         if arraySel1[j] < arraySel1[minI]:
             minI = j
     arraySel1[i], arraySel1[minI] = arraySel1[minI], arraySel1[i]
     print(f"This is selection sorted: {arraySel1}")

def main():
    selectSort(arraySel1)
    print(arraySel1)

if __name__ == "__main__":
    main()