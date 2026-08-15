### Problem: Left rotate an array by D places

arr = [1,2,3,4,5,6,7]
n = len(arr)
d = int(input("Enter the number of left rotate places:"))

## Brutal force Approch 

print("Before rotation Array:",arr)

def left_rotate(arr,n,d):
    d = d % n
    temp = [0]*d

    for i in range(d):
        temp[i] = arr[i]

    for i in range(d,n):
        arr[i-d] = arr[i]

    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]

    print("After rotataion Array:",arr)

left_rotate(arr,n,d)


## Optimal Approch:

def reverse(arr,left,right):

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1

def left_Rotation(arr,n,d):

    d = d % n 
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

    print(arr)

left_Rotation(arr,n,d)



