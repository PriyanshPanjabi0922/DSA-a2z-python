### Find the Intersection array from two given sorted array

arr1 = [1,2,3,4,5,5,6]
arr2 = [1,1,2,3,4,6,7]
n1 = len(arr1)
n2 = len(arr2)

### Brutal Force Approch:

def intersection_Arr(arr1,arr2,n1,n2):
    visited_arr = [0]*n2
    result = []
    for i in range(n1):
        for j in range(n2):
            if arr1[i] == arr2[j] and visited_arr[j] == 0:
                result.append(arr1[i])
                visited_arr[j] = 1
                break
            if arr2[j] > arr1[i]:
                break

    print(result)

intersection_Arr(arr1,arr2,n1,n2)


### Optimal Approch:

def insertion_arr(arr1,arr2,n1,n2):
    Result = []

    i = 0
    j = 0

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            i+=1
        elif arr1[i] > arr2[j]:
            j+=1
        else:
            Result.arr1[i]
            i+=1
            j+=1

    print(Result)

intersection_Arr(arr1,arr2,n1,n2)



