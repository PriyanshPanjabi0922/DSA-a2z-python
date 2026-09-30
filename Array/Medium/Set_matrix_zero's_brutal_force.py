matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

rows = len(matrix)
cols = len(matrix[0])
answer_matrix = [[ ] * rows for _ in range(rows)]
zero_row = (set())
zero_col = (set())
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_row.add(i)
            zero_col.add(j)


for i in range(rows):
    for j in range(cols):
        if i in zero_row or j in zero_col:
            answer_matrix[i].append(0)
        else:
            answer_matrix[i].append(matrix[i][j])

print(answer_matrix)
            
