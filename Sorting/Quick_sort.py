### Quick sort:

arr = [7,3,5,1,7,3,9]
low = 0
high = len(arr) -1

print("before sorting:",arr)

def helper_quick_sort(arr,low,high):

    pivot = low

    i = low
    j = high

    while i <j :
        while i <= high -1 and arr[i] <= arr[pivot]:
            i+=1
        while j >=low+1 and arr[j] > arr[pivot] :
            j-=1

        if i <j:
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[low],arr[j] = arr[j],arr[low]

    return j

def quick_sort(arr,low,high):

    if low < high:
        p_index = helper_quick_sort(arr,low,high)
        quick_sort(arr,low,p_index-1)
        quick_sort(arr,p_index+1,high)


quick_sort(arr,low,high)
print("after sort",arr)








