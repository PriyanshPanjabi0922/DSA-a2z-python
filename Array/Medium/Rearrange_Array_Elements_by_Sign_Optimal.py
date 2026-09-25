arr = [3,2,-3,-1,5,-9]
n = len(arr)
result = [0]*n
pos_index = 0
neg_index = 1

for i in range(n):
    if arr[i] > 0:
        result[pos_index] = arr[i]
        pos_index+=2
    else:
        result[neg_index] = arr[i]
        neg_index+=2

print(result)