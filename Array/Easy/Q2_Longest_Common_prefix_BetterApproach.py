### find the longest common prefix

arr = ["Flower","Flow","Fluied"]
n = len(arr)

## Better Solution

def Longest_common_prefix_2(arr):
    prefix = arr[0]

    for word in arr[1:]:
        i = 0

        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i+=1
        prefix = prefix[:i]

    return prefix

result = Longest_common_prefix_2(arr)
print(result)