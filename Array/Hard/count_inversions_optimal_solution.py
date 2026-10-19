nums = [2,3,7,1,3,5]

low = 0
high  = len(nums) - 1

def merge(nums,low,mid,high):

    temp = []
    left = low
    right = mid + 1
    count = 0

    while left <= mid and right <= high :
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1
            count+= mid-left+1

    while left <=mid:
        temp.append(nums[left])
        left+=1

    while right <= high:
        temp.append(nums[right])
        right+=1

    for i in range(low,high+1):
        nums[i] = temp[i - low]

    return count

def merge_sort(nums,low,high):

    if low >= high:
        return 0
    
    mid = (low +high )//2

    left_count = merge_sort(nums, low, mid)
    right_count = merge_sort(nums, mid + 1, high)
    merge_count = merge(nums, low, mid, high)

    return left_count + right_count + merge_count

result = merge_sort(nums,low,high)
print(result)