# Bubble sort!
arr = [12,45,20,52,9]
n = len(arr)

print("Before Sort:",arr)
for i in range(n-1,0,-1): \

    for j in range(0,i,1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp

print("After sort:",arr)

## Time Complacity: n^2 for worst and average case but for 'best' it is n (ex, 1 2 3 4 5) 

