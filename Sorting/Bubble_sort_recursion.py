## solving the bubble sort using recursion!!

arr = [12,45,20,52,9]
n = len(arr)

print("Before sorting:",arr)

def bubble_sort(arr,n):

    if n == 1:
        return
    is_swap = False

    for i in range(n-1):

        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            is_swap  = True

    if not is_swap:
        return

    bubble_sort(arr,n)

bubble_sort(arr,n)

print("After sorting:",arr)
