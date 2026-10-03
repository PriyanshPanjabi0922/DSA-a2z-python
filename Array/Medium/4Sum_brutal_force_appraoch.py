nums = [1,2,3,4]
target = 100

def solution(nums,target):
    n = len(nums)
    answer = []

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for m in range(k+1,n):
                    if nums[i] + nums[j] +nums[k] + nums[m] == target:
                        quadruplets = [nums[i], nums[j],nums[k] ,nums[m]]

                        if quadruplets not in answer:
                            answer.append(quadruplets)

    return answer

result = solution(nums,target)
print(result)