### Problem: right rotate an array by D places

arr = [1,2,3,4,5]
n = len(arr)
d = int(input("Enter a valid integer number:"))

## Brutal Force Approch:

def right_rotate(arr,n,d):
    d = d % n

    temp = [0] * d

    for i in range(d):
        temp[i] = arr[n-d+i]

    for i in range(n-d-1,-1,-1):
        arr[i+d] = arr[i]

    for i in range(d):
        arr[i] = temp[i]

    print(arr)

right_rotate(arr,n,d)

## Optimal Approch:

def reverse(arr,left,right):

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right -=1

def right_Rotate(arr,n,d):
    d = d % n

    reverse(arr,n-d,n-1)
    reverse(arr,0,n-d-1)
    reverse(arr,0,n-1)

    print(arr)

right_Rotate(arr,n,d)