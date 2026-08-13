### Check is the array is sorted?

arr = [1,2,3,4,5,5,5,6,7]
n = len(arr)
def is_sorted(arr,n):
    for i in range(1,n):
        if arr[i]>= arr[i-1]:
            pass
        else:
            return False 
    return True

print(is_sorted(arr,n))
