nums = [2,0,2,1,1,0] 

def solution(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):

            if nums[j] < nums[i]:
                nums[j],nums[i] = nums[i],nums[j]

    return nums

result = solution(nums)
print("result:",result)