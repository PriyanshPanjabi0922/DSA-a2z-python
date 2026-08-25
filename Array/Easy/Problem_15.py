### Longest subarray with given sum k(Positive)

arr = [1,2,3,6,8,4]
n = len(arr)
k = 6

# Brurtal approach:

def Longest_subarray(arr,n,k):

    result_list = []
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == k:
                result_list.append(j-i+1)

    print("Longest subarray :",max(result_list))
     
Longest_subarray(arr,n,k)

# Better Approach:

def longest_subarray(arr,n,k):
    max_legth = 0
    length = 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if sum == k:
                length = j - i + 1
                if max_legth < length:
                    max_legth = length

    print("Longest subarray :",max_legth)

longest_subarray(arr,n,k)

# More Better Approach:

def longest_subarray(arr,n,k):
    longest_len = 0
    prefix_sum = 0
    prefix_map = {

    }

    for  i in range(n):
        prefix_sum += arr[i]

        if prefix_sum == k:
            longest_len = i + 1
        
        if (prefix_sum - k) in prefix_map:
            longest = i - prefix_map[prefix_sum - k]
            if longest_len < longest:
                longest_len = longest

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    print(f"Longest sub-array: {longest_len}")

longest_subarray(arr,n,k)

## Optimal Approach:

def Longest_SubArray(arr,n,k):
    left = 0
    right = 0
    max_length = 0
    sum  = arr[0]

    while right < n:
        while left <= right and sum > k:
            sum -= arr[left]
            left+=1

        if sum == k:
            max_length = max(max_length,right - left +1)
        right+=1

        if right < n :
            sum += arr[right]

    print("Longest Sub_Array:",max_length)

Longest_SubArray(arr,n,k)           







