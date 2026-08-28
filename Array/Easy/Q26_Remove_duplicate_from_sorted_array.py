### Remove Duplicates from Sorted Array

# Brutal Force Approach:

nums =[0,0,0,1,2,3,4,4,5,5,7]
n = len(nums)

def Duplicates_problem(nums,n):
    position = 1
     
    for i in range(n):
            
        if nums[i] != nums[i-1]:
            nums[position] = nums[i]
            position+=1

    return position

Duplicates_problem(nums,n)

