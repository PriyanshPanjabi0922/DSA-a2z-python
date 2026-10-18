nums = [3,4,5,1,2,1]

def solution(nums):
    n = len(nums)
    repeating = -1
    missing = -1

    hasharr = [0]*(n+1)

    for i in range(n):
       
        hasharr[nums[i]] +=1

    for i in range(1,n+1):
        if hasharr[i] ==2:
            repeating = i

        elif hasharr[i] ==0:
            missing = i

        if repeating != -1 and missing != -1:
            break

    return [repeating,missing]

answer = solution(nums)
print(answer)