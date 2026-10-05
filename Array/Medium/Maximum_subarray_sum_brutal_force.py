
nums = [5,4,-1,7,8]

def solution(nums):
    n = len(nums)

    maximum = nums[0]

    for i in range(n):
        for j in range(i,n):
            sum = 0
            for k in range(i,j+1):
                sum += nums[k]

            maximum =max(sum,maximum)

    return maximum

result = solution(nums)
print(result)

    