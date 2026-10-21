nums = [2,3,-2,4]

def solution(nums):
    n = len(nums)
    maxi = nums[0]

    prefix = 1
    suffix = 1

    for i in range(n):
        if prefix ==0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *=nums[i]
        suffix *=nums[n-i-1]

        maxi = max(maxi,prefix,suffix)

    return maxi

answer = solution(nums)
print(answer)