nums = [2,3,-2,4]

def solution(nums):
    n = len(nums)
    maxi = nums[0]

    for i in range(n):
        for j in range(i,n):
            product = 1
            for k in range(i,j+1):
                product*=nums[k]

                if maxi < product:
                    maxi = product


    return maxi
answer = solution(nums)
print(answer)
