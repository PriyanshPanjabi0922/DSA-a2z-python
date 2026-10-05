
nums = [-2,1,-3,4,-1,2,1,-5,4]

def solution(nums):
    n = len(nums)

    maximum = nums[0]

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            maximum =max(sum,maximum)

    return maximum

result = solution(nums)
print(result)

    