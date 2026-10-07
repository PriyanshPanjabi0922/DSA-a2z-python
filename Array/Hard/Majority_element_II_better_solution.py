nums = [-12,-12,-12]

def solution(nums):
    n = len(nums)
    answer = []

    dict1 = {

    }

    for i in range(n):
        if nums[i] not in dict1:
            dict1[nums[i]] = 1
        else:
            dict1[nums[i]] +=1

    for key,value in dict1.items():
        if value > n//3:
            answer.append(key) 

        if len(answer) == 2:
            break

    return answer

result = solution(nums)
print(result)