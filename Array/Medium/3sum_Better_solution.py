nums = [-1,0,1,2,-1,-4]

answer = []

def solution(nums,answer):
    n = len(nums)

    for i in range(n):
        seen = set()
        for j in range(i+1,n):

            needed = -(nums[i] + nums[j])

            if needed in seen:
                triplet = [nums[i],nums[j],needed]
                triplet.sort()

                if triplet not in answer:
                    answer.append(triplet)
            
            seen.add(nums[j])

    return answer

result = solution(nums,answer)
print(result)


