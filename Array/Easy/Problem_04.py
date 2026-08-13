## Remove duplicate from the sorted array

arr = [1,1,2,2,2,3,4,5,5,6]

# Brutal :
unique = set()

for i in arr:
    if i not in unique:
        unique.add(i)

print(f"set of unique element in this array:{unique} and its length is :{len(unique)}")
    

# Optimal

def chech_sort(arr):
    i = 0
    j = 1

    while j < len(arr):
        if arr[j] == arr[i]:
            pass
        else:
            i+=1
            arr[i] = arr[j]

        j+=1

    print(f"Total unique element are {i+1}")

chech_sort(arr)
print(arr)
        

    

