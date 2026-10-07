nums = [1,2,1,2,2,3,3,1]

def solution(nums):
    n = len(nums)
    answer = []
    count1,count2 = 0,0
    el1 = float('-inf')
    el2 = float('-inf')

    for i in range(n):

        if count1 == 0 and el2 != nums[i]:
            count1+=1
            el1 = nums[i]

        elif count2 == 0 and el1 != nums[i]:
            count2+=1
            el2 = nums[i]

        elif nums[i] == el1:
            count1+=1
        elif nums[i] ==el2:
            count2+=1

        else:
            count1 -=1
            count2 -=1

    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if el1 == nums[i]:
            cnt1+=1
        if el2 == nums[i]:
            cnt2+=1
    minimum = n//3

    if cnt1 > minimum:
        answer.append(el1)
    if cnt2 > minimum:
        answer.append(el2)

    return answer

result = solution(nums)
print(result)
    

