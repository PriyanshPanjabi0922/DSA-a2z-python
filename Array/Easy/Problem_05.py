## Problem: Left Rotate an array by one place

arr = [1,2,3,4,5]
n = len(arr)
def left_rotate(arr,n):
    temp = arr[0]

    for i in range(n):
        arr[i-1] = arr[i]

    arr[n-1] = temp

    print(arr)

left_rotate(arr,n)
