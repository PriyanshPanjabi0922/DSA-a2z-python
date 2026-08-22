### Problem : find maximul consecative one's

arr = [0,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1]

## Brutal Approach:

def max_ones(arr):
    n = len(arr)
    li1 = []
    val = 0

    for i in range(n):
        if arr[i] == 1:
            val+=1
        if arr[i] != 1:
            li1.append(val)
            val = 0
    li1.append(val)    
        
    print(max(li1))

max_ones(arr)

## Optimal Approach:

def Max_ones(arr):
    n = len(arr)
    val = 0

    for i in range(n):
        if arr[i] == 1:
            val+=1
        if arr[i] != 1:
            max_one = val
            val = 0

    max_one = val
        
    print(max_one)

Max_ones(arr)