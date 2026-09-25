nums = [3,1,-2,-5,2,-4]
n = len(nums)
pos_arr = []
neg_arr = []
for i in range(n):

    if nums[i] > 0:
        pos_arr.append(nums[i])
    else:
        neg_arr.append(nums[i])


for i in range(n//2):

    nums[i*2] = pos_arr[i]
    nums[i*2+1] = neg_arr[i]

print(nums)

