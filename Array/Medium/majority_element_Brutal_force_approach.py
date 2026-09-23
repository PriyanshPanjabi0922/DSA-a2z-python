nums = [2,2,1,1,1,2,2]
n = len(nums)
def majority_element(arr,n):
    for i in range(n):
        count = 0

        for j in range(n):
            if nums[j] == nums[i]:
                count+=1

        if count > (n/2):
            return nums[i]

result = majority_element(nums,n)
print(result)
