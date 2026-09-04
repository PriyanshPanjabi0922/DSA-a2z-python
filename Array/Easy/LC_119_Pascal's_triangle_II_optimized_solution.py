rowIndex = 5

def Pascal_Triangle_II(rowIndex):
    row = [1]
    current = 1

    for i in range(1,rowIndex+1):

        next = current * (rowIndex - i + 1) // i
        current = next
        
        row.append(next)

    return row


ans = Pascal_Triangle_II(rowIndex)
print(ans)