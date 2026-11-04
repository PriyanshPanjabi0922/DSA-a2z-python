nums = [-1,2,1,-4]
target = 1
def solution(nums,target):
    best_diff = float('inf')
    closests_sum = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                curr_sum = nums[i] + nums[j] + nums[k]
                difference= abs(curr_sum - target)

                if difference < best_diff:
                    best_diff = difference
                    closests_sum = curr_sum

    return closests_sum

answer = solution(nums,target)
print(answer)