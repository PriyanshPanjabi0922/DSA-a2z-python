nums = [2,3,7,1,3,5]

def solution(nums):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                count+=1

    return count

answer = solution(nums)
print(answer)
