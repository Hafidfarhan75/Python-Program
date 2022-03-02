def bubbleSort(arr):
    n = len(arr)
    temp = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j+1]
                arr[j + 1] = arr[j]
                arr[j] = temp

arr = [2,3,1,7,4,9,0,6,5,10]

print("Sebelum di Shorting : ")
for i in range(len(arr)):
    print(arr[i], end=" ")

bubbleSort(arr)
print()

print("Sesudah di Shorting : ")
for i in range(len(arr)):
    print(arr[i], end=" ")