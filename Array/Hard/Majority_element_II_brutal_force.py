nums = [-12,-12,-12]

def solution(nums):
    n = len(nums)
    answer = []

    for i in range(n):
        if len(answer) == 0 or answer[0] is not nums[i]:
            count = 0
            for j in range(n):
        
                if nums[j] == nums[i]:
                    count+=1

            if count > n//3:
                    answer.append(nums[i])


            if len(answer) == 2:
                 break

    return answer


result = solution(nums)
print(result)
