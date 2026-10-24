nums1 = [1,3]
nums2 = [2,5]


def solution(nums1,nums2):
    
    left = 0
    right = 0
    current = 0
    previous = 0

    m =len(nums1)
    n = len(nums2)

    total = m + n
    count = 0
    while count < (total // 2) + 1:
        previous = current

        if left == len(nums1):
            current = nums2[right]
            right+=1

        elif right == len(nums2):
            current = nums1[left]
            left +=1

        else:
            if nums1[left] < nums2[right]:
                current = nums1[left]
                left+=1
            else:
                current = nums2[right]
                right+=1

        count+=1

    if total %2 == 0:
        return (current + previous) / 2
    else:
        return current

result = solution(nums1,nums2)
print(result)