matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

n = len(matrix)

answer = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        answer[j][n-1-i] = matrix[i][j]

print(answer)