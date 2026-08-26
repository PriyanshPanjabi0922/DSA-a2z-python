### Problem name: Two Sum

arr = [2,4,1,7,9,11,15]
target = 5

## Optimal Approach:

def Solution(arr,target):
    n = len(arr)
    seen = {}

    for i in range(n):
        current = arr[i]
        needed = target - current

        if needed in seen:
            return [seen[needed],i]

        else:
            seen[current] = i


answer = Solution(arr,target)

print(answer)