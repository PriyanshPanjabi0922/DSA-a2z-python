nums = [1,-2,2,4,-4]

def solution(nums):
    n = len(nums)
    longest =0

    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum+= nums[j]
            if curr_sum == 0:
                length = j-i+1
                longest = max(longest,length)

    return longest

answer = solution(nums)
print(answer)