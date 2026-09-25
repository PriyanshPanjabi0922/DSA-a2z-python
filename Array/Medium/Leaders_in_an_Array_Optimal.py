arr = [10,22,12,4,0,6]
n = len(arr)
result_array = []
max = float("-inf")

for i in range(n-1,0,-1):

    if arr[i] > max:
        max = arr[i]
        result_array.append(max)

print(result_array)