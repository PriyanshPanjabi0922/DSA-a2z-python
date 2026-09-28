n = int(input("Eter a number :"))

previous = [1]
result = []
result.append(previous)

for i in range(n-1):
    new_row = [1]

    for j in range(len(previous)-1):
        new_row.append(previous[j] + previous[j+1])

    new_row.append(1)

    previous = new_row
    result.append(previous)

print(result)