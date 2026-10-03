nums = [1,0,-1,0,-2,2]
target = 0

def solution(nums,target):
    nums.sort()
    n = len(nums)
    answer = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1] :
            continue

        for j in range(i+1,n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            k = j+1
            m = n-1

            while k < m:

                sum = nums[i] + nums[j] + nums[k] + nums[m]

                if sum == target:
                    quadruplets = [nums[i],nums[j],nums[k],nums[m]]
                    answer.append(quadruplets)
                    k+=1
                    m-=1

                    while k < m and nums[k] == nums[k-1]:
                        k+=1
                    while k < m and nums[m] == nums[m+1]:
                        m-=1
                    
                elif sum > target:
                    m-=1
                else:
                    k+=1

    return answer

result = solution(nums,target)
print(result)

