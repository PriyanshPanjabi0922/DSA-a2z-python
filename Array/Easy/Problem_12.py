### find the missing number from an array

arr = [1,2,4,5]
n = len(arr)
## Brutal force Approach:

def missing_number1(arr,n):

    for i in range(1,n+1):
        flag = 0

        for j in range(n):
            
            if arr[j] == i:
                flag = 1
                break
            
        if flag == 0:
            print(f"Missing number is {i} using brutal force Approach")     

missing_number1(arr,n)

## Better Approach:

def missing_number2(arr,n):
    hash_arr = [0] * (n+2)
    
    for i in range(n):
        hash_arr[arr[i]] = 1

    for i in range(1,n+2):
        if hash_arr[i] == 0:
            print(f"Missing number is {i} using Better Approach")

missing_number2(arr,n)

### Optimal Approach 1:

def missing_number3(arr,n):
    N = n+1
    sum = N*(N+1)/2
    chech_sum = 0

    for i in range(n):
        chech_sum += arr[i]

    print(f"Missing number is {int(sum - chech_sum)} using Optimal Approach 1")

missing_number3(arr,n)

### Optimal Approach 2:

def missing_number4(arr,n):

    xor =0

    for i in range(1,n+2):
        xor ^= i

    for i in range(n):
        xor ^= arr[i]

    print(f"Missing number is {xor} using Optimal Approach 2")

missing_number4(arr,n)