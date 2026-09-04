## Pascal's triangle I

numRows = 0

def pascal_triangle(numRows):

    result = []

    for row in range(numRows):
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

    return result

answer = pascal_triangle(numRows)

print(answer)

