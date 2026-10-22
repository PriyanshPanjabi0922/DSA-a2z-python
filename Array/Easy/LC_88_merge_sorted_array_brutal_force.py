nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m =3
n = 3

def solution(nums1,nums2,m,n):
    answer_array = []
    for i in range(m):
        answer_array.append(nums1[i])
    for i in range(n):
        answer_array.append(nums2[i])
    answer_array.sort()
    for i in range(m+n):
        nums1[i] = answer_array[i]

    return nums1

answer = solution(nums1,nums2,m,n)
print(answer)