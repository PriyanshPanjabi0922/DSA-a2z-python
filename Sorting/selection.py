# SELECTION SORT!

arr = [23,12,9,44,22]
n = len(arr)

print("Before sort:",arr)

for i in range(n-1):
    min = i
    for j in range(i,n):
        if arr[j] < arr[min]:
            min = j

    temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp

print("After sort:",arr)

# selection sort , TIME COMPLECITY: best = worst = avg = n^2

