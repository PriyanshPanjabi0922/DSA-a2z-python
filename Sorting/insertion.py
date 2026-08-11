# Insertion sort! 

arr = [9,12,13,15,8,6,11]
n = len(arr)
print("Before sort:",arr)
for i  in range(n):
    j = i
    while j>0 and arr[j-1] > arr[j]:  # >0 not >= bcz j-1 for 0 will give -1 if consider >=
        temp = arr[j-1]
        arr[j-1] = arr[j]
        arr[j] = temp

        j-=1

print("After sort:",arr)

# time complacity : best case = O(n){bcz no swap} while for worst and avg = O(n^2)

