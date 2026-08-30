### Seach insert Position

nums = [1,3,5,6]
target = 5

## Brutal force Approach:

def Seach_insert_Position(nums,target):
    n = len(nums)
    for i in range(n):

        if nums[i] >= target:
            return i 
        
    return n

result = Seach_insert_Position(nums,target)
print(result)

