## insertion sort using recusion

arr = [9,12,13,15,8,6,11]
n = len(arr)
print("Before sort:",arr)

def insertion_sort(arr,i,n):

    if i == n:
        return

    j =i

    while j>0 and arr[j-1] > arr[j]:
        arr[j],arr[j-1] = arr[j-1],arr[j]
        
        j-=1

    insertion_sort(arr,i+1,n)

insertion_sort(arr,0,n)

print("After sorting:",arr)

        