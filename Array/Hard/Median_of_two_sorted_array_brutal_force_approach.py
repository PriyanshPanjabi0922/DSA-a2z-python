nums1 = [1,3]
nums2 = [2,5]

def solution(nums1,nums2):
    m = len(nums1)
    n = len(nums2)
    answer_arr = []

    for i in range(m):
        answer_arr.append(nums1[i])

    for i in range(n):
        answer_arr.append(nums2[i])

    answer_arr.sort()
    answer_arr_len = len(answer_arr)

    check = answer_arr_len % 2

    if check != 0:
        return answer_arr[answer_arr_len//2]

    else:
        ans = answer_arr[answer_arr_len//2] + answer_arr[(answer_arr_len//2) + 1]
        return ans / 2

result = solution(nums1,nums2)
print(result)

    