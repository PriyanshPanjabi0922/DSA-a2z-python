nums = [2,2,1,1,1,2,2]
n = len(nums)

def majority_element(nums,n):
    count = 0

    for i in range(n):

        if count == 0:
            el = nums[i]
            count = 1

        elif nums[i] == el:
            count +=1

        else:
            count -=1

        return el

result = majority_element(nums,n)
print(result)

