### find the longest common prefix

arr = ["Flower","Flow","Fluied"]
n = len(arr)

# Brutal Force Approach:

def Longest_common_prefix(arr,n):
    prefix = ""
    for i in range(len(arr[0])):
        for j in range(1,n):

            if i >= len(arr[j]):
                return ""

            if arr[0][i] != arr[j][i]:
                return prefix 

        prefix += arr[0][i]
        
    return prefix

solution = Longest_common_prefix(arr,n)
print(solution)

