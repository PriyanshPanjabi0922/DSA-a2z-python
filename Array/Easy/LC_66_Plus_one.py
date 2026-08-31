## Plus one

digit = [9,9,9,9,9,9]

def plus_one(digit):
    n = len(digit)

    for i in range(n-1,-1,-1):
        if digit[i] == 9:
            digit[i] = 0
        else:
            digit[i]+=1
            return digit
    
    return [1] + digit

result = plus_one(digit)
print(result)