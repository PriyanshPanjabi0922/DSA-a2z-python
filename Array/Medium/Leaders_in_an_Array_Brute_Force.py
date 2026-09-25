arr = [10,22,12,4,0,6]
n = len(arr)
result_array = []

for i in range(n):
    isLeader = True

    for j in range(i+1,n):

        if arr[j] > arr[i]:
            isLeader = False
            break

    if isLeader:
        result_array.append(arr[i])

print(result_array)