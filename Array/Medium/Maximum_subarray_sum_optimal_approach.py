nums = [5,4,-1,7,8]

def solution(nums):
    n = len(nums)

    current_sum = 0
    max_sum = nums[0]

    for i in range(n):
        current_sum = max(nums[i],current_sum+nums[i])
        max_sum = max(max_sum,current_sum)

    return max_sum

result= solution(nums)
print(result)