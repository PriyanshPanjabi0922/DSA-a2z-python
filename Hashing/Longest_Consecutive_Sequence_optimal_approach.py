nums = [1,192,1,2,199,100,101,104,103,102,3]

def solution(nums):
    n = len(nums)
    nums_set = set(nums)
    longest = 0

    for i in nums_set:
        if i - 1 not in nums_set:
            x = i
            cnt = 1

            while x + 1 in nums_set:
                x +=1
                cnt+=1

            longest = max(longest,cnt)

    return longest

result = solution(nums)
print(result)
