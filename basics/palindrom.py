### Reverse the string using the two parameterize

arr = [1,2,3,4,5,6,4,4,4,5,5,7,89]

left = 0
right = len(arr) - 1


def reverse_arr(arr,left,right):
    if left >= right:
        return

    arr[left],arr[right] = arr[right],arr[left]

    reverse_arr(arr,left+1,right-1)

reverse_arr(arr,left,right)
print(arr)

### Reverse the string using the one  parameter

arr = [1,2,3,4,5,6,4,4,4,5,5,7,89]
i = 0

def revrse_Arr(arr,i):

    left = i
    right = len(arr)-i-1

    if i >= len(arr) // 2:
        return

    arr[left],arr[right] = arr[right],arr[left]

    revrse_Arr(arr,i+1)

revrse_Arr(arr,i)
print(arr)    

### Palindrom or not?  : 

string = "MADAM"
i = 0
def is_palindrom(string,i):
    left = i
    right = len(string)-i-1

    if i >= len(string) // 2:
        return True

    if string[left] != string[right]:
        return False

    return is_palindrom(string,i+1)

result = is_palindrom(string,i)
print(result)

    

