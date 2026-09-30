matrix = [
    [1,0,3],
    [4,5,6],
    [7,8,0]
]
rows = len(matrix)
cols = len(matrix[0])
answer_matrix = [[1] * cols for _ in range(rows)]

row_index = [0] * rows
col_index = [0] * cols

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            row_index[i] +=1
            col_index[j] +=1

for i in range(rows):
    for j in range(cols):

        if row_index[i] > 0 or col_index[j] > 0:
            answer_matrix[i][j] = 0
        else:
            answer_matrix[i][j] = matrix[i][j]

print(answer_matrix)
