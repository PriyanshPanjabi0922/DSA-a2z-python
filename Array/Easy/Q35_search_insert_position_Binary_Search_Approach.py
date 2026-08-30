### Seach insert Position

nums = [1,3,5,6]
target = 5

## Binary Search Approach:

def Search_Insert_Position(nums,target):
    n = len(nums)

    start = 0
    end = n 

    while start < end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid

    return start
result2 = Search_Insert_Position(nums,target)

print(result2)