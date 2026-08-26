### Problem name: Two Sum

arr = [2,4,1,7,9,11,15]
target = 15

## Brutal force approach:

def solution(arr,target):
    n = len(arr)

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return i,j
            else:
                j+=1
        i+=1

answer = solution(arr,target)
print(answer)


