nums = [2,2,1,1,1,2,2]
n = len(nums)

def majority_element(nums,n):
    freq = {}

    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1

    for key,value in freq.items():
        if value > n//2:
            return key

result = majority_element(nums,n)
print(result)