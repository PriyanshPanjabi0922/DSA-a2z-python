nums = [1,-2,2,-4,4]

def solution(nums):
    n = len(nums)
    prefix_map = {}
    prefix_sum = 0
    longest = 0

    for i in range(n):
        prefix_sum += nums[i]

        if prefix_sum == 0:
            longest = max(longest,i + 1)

        elif prefix_sum in prefix_map:
            length = i - prefix_map[prefix_sum] 
            longest = max(longest,length)

        else:
            prefix_map[prefix_sum] = i 

    return longest

answer = solution(nums)
print(answer)
