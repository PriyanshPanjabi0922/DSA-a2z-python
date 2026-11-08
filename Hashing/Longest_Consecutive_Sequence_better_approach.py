nums = [1,192,1,2,199,100,101,104,103,102,3]

def solution(nums):
    n = len(nums)
    if not nums:
        return 0

    nums.sort()
    last_smallest = nums[0]
    longest = 1
    curr_count = 1

    for i in range(1,n):

        if nums[i] == last_smallest:
            continue
        elif nums[i] == last_smallest +1:
            curr_count +=1
        else:
            curr_count =1
        last_smallest = nums[i]

        longest = max(longest,curr_count)
    return longest

result = solution(nums)
print(result)