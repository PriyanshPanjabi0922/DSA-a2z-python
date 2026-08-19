### Find the unino array from the given sorted array

arr1 = [1,1,2,3,4,4,5,5,5,5,5,5,333]
arr2 = [1,2,3,4,5,5,6,7,8]
n1 = len(arr1)
n2 = len(arr2)

## Brutal force Approch:

def union_set(arr1,arr2):
    
    union = set()

    for i in arr1:
        union.add(i)

    for i in arr2:
        union.add(i)

    union_arr = list(union)

    print(union_arr)

union_set(arr1,arr2)

## Optimal Solution:

def Union_set(arr1,arr2,n1,n2):

    print("Function is started")
    i = 0
    j = 0
    Union_Arr = []

    while i < n1 and j < n2:
       
        if arr1[i] < arr2[j]:
            if not Union_Arr or Union_Arr[-1] != arr1[i]:
                Union_Arr.append(arr1[i])
            i+=1

        elif arr2[j] < arr1[i]:
            if not Union_Arr  or Union_Arr[-1] != arr2[j]:
                Union_Arr.append(arr2[j])
            j+=1

        else:
            
            if not Union_Arr  or Union_Arr[-1] != arr1[i]:
                Union_Arr.append(arr1[i])
            i+=1
            j+=1
            

    while i < n1:
            if not Union_Arr or Union_Arr[-1] != arr1[i]:
                Union_Arr.append(arr1[i])
            i+=1

    while j < n2:
            if not Union_Arr or Union_Arr[-1] != arr2[j]:
                Union_Arr.append(arr2[j])
            j+=1

    print(Union_Arr)


Union_set(arr1,arr2,n1,n2)





