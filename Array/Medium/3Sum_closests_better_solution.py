nums = [1,1,1,1]
target = 0

def solution(nums,target):
    n = len(nums)
    closests_sum = 0
    best_diff = float('inf')

    nums.sort()
    for i in range(n-2):
        left = i+1
        right = n-1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            differnece = abs(curr_sum - target)

            if differnece < best_diff:
                best_diff = differnece
                closests_sum = curr_sum

            if curr_sum == target:
                return target
            if curr_sum < target:
                left+=1
            else:
                right-=1

    return closests_sum

answer = solution(nums,target)
print(answer)
                