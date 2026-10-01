nums = [3,2,8,4]
target = 6
dict1 = {
        
    }

def two_sum(nums,target,dict1):
    n = len(nums)

    for i in range(n):
        

        current = nums[i] 
        needed = target - current

        if needed in dict1:
            return [dict1[needed],i]
        else:

            dict1[current] = i

    return "Not Possible"

answer = two_sum(nums,target,dict1)
print(answer)
