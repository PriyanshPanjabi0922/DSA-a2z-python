nums = [1,2.3]
def solution(nums):
    n = len(nums)
    permuatation = []
    used = [False] * n
    current = []

    def under_solution():
        if len(current) == n:
            permuatation.append(current.copy())
            return 

        for i in range(n):

            if not used[i]:
                current.append(nums[i])
                used[i] = True

                under_solution()

                current.pop()
                used[i] = False

    under_solution()
    permuatation.sort()

    for i in range(len(permuatation)):
        if permuatation[i] == nums:
            while i + 1< len(permuatation) and permuatation[i+1] == nums:
                i+=1

            if i == len(permuatation)-1:
                nums[:] = permuatation[0]
            else:
                nums[:] = permuatation[i+1]
            return

solution(nums)
print(nums)