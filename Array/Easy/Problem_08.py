### Problem : move all zero to the end of an array

arr = [1,2,0,3,2,0,0,1,6,2,0,8]
n = len(arr)

## Brutal Force Approch:
def move_zeros(arr,n):
    temp = []

    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp),n):
        arr[i] = 0

    print("Brutal force Approch Answer:",arr)

move_zeros(arr,n)

## Optimal Approch:

def move_zero_optimal(arr,n):
    
    j = -1

    for i in range(n):
        if arr[i] == 0:
            j = i
            break

    for i in range(j+1,n):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]

            j+=1

    print("Optimal Approch answer:",arr)

move_zero_optimal(arr,n)