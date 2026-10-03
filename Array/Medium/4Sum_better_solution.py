nums = [1,0,-1,0,-2,2]
target = 0

def solution(nums,target):
    n = len(nums)
    answer = []

    for i in range(n):
        for j in range(i+1,n):
            seen = set()
            for k in range(j+1,n):
                sum = nums[i] + nums[j] + nums[k]

                fourth = target - sum

                if fourth in seen:
                    quadruplets = [nums[i],nums[j],nums[k],fourth]
                    quadruplets.sort()

                    if quadruplets not in answer:
                        answer.append(quadruplets)

                seen.add(nums[k])

    return answer

result = solution(nums,target)
print(result)
                    