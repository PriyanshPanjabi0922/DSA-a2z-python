nums = [2,3,-2,4]

def solution(nums):
    n = len(nums)
    maxi = nums[0]
    
    for i in range(n):
        previous = 1
        for j in range(i,n):
            previous*=nums[j]

            if maxi < previous:
                maxi = previous

    return maxi

answer = solution(nums)
print(answer)