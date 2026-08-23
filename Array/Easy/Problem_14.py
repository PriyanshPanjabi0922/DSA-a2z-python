## find a number which is once present in an non-empty array where other number are twice in that array

arr = [4,1,2,1,2,4,9,9,8]
n = len(arr)
require_arr_max = max(arr) +1

## Brutal force appraoch:

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count +=1
            
    if count == 1:
        print(arr[i])
        
## Better Approach: (Using hashing)

hash_arr = [0] * require_arr_max

for i in range(n):
    hash_arr[arr[i]] +=1

if hash_arr[arr[i]] == 1:
    print(arr[i])

# Optimal Approach:

xor = 0

for i in range(n):
    xor = xor ^ arr[i]

print(xor)
