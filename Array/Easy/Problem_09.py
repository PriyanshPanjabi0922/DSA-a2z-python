#### Problem : linear Search

arr = [12,34,5,2,12,4,76,4]
n = len(arr)
num = int(input("Enter a number in integer only:"))

def linear_search(arr,n,num):
    is_found = False
    for i in range(n):
        if arr[i] == num:
            is_found = True    
            break

    if is_found:
        print(f"First occurence of {num} is {i}")
    else:
        print(f"there is no {num} in the array")


linear_search(arr,n,num)