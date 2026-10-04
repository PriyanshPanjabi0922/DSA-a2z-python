nums= [2,0,2,1,1,0]

def solution(num):
    n = len(nums)
    low = 0
    mid = 0
    high = n-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid] == 1:
            mid+=1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high-=1

    return nums

result = solution(nums)
print(result)
