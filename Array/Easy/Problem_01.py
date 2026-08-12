## largest element in an array

# Brutal force approch: 

arr = [3,2,1,2,1]
n = len(arr)
print(f"given array:{arr}")

for i in range(n-1,0,-1):

    for j in range(0,i,1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]


print(f"largest element from the given array :{arr[n-1]}")


## Optimal Solution:

arr = [3,2,1,2,1]
Largest = arr[0]

for element in arr:
    
    if Largest < element:
        Largest = element

print("Largest element is :",max)
