nums = [3,4,2,1,1,5]

def solution(nums):
    n = len(nums)

    SN = (n * (n+1))/2
    S2N = (n * (n+1) * (2*n+1))/6

    S = 0
    S2 = 0

    for i in range(n):
        S += nums[i]
        S2 += nums[i] * nums[i]

    val1 = S - SN
    val2 = S2 - S2N
    val2 = val2 /val1

    x = int((val1 + val2) / 2)
    y = int(x - val1)

    return [x,y]

answer = solution(nums)
print(answer)