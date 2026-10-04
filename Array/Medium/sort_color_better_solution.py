nums= [2,0,2,1,1,0]

def solution(nums):
    n = len(nums)
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(n):

        if nums[i] == 0:
            count_0+=1
        elif nums[i] == 1:
            count_1+=1
        else:
            count_2+=1

    for i in range(count_0):
        nums[i] = 0

    for i in range(count_0,count_0+count_1):
        nums[i] = 1

    for i in range(count_0+count_1,count_0+count_1+count_2):
        nums[i] = 2

    return nums

result = solution(nums)
print(result)
    