### Problem : remove element

nums = [0,1,2,3,3,4,5,6,4,7,3,9]
val = 5

def Remove_element(nums,val):
    n = len(nums)
    position = 0

    for i in range(n):
        if nums[i] != val:
            nums[position] = nums[i]
            position+=1

    return position

Remove_element(nums,val)