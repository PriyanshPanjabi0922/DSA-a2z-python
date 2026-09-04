## Pascal's Triangle II


rowIndex = 5

def pascal_triangle_II(rowIndex):

    result = []

    for row in range(rowIndex+1):
        if row == 0:
            new_row = [1]
            result.append(new_row)
            continue

        previous = result[-1]
        new_row = [1]

        for i in range(len(previous)-1):
            new_row.append(previous[i] + previous[i+1])

        new_row.append(1)
        result.append(new_row)

    return result[-1]

answer = pascal_triangle_II(rowIndex)

print(answer)










