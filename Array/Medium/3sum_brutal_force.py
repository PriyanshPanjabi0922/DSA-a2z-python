nums = [-1,0,1,2,-1,-4]

answer = []

def solution(nums,answer):
    n= len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                                
                if nums[i] + nums[j] + nums[k] == 0 :
                    triplet = [nums[i],nums[j],nums[k]]
                    triplet.sort()

                    if triplet not in answer:
                        answer.append(triplet)
                    
    return answer

result = solution(nums,answer)
print(result)


