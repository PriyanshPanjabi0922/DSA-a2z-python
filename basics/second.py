# 1: print name 5 times

n = int(input("Enter a number:"))
count = 0

def print_name():
    global count

    if count > n:
        return

    print("Priyansh")
    count+=1

    print_name()

print_name()

''' Optimal approch for this question can be like: '''

n = int(input("Enter a number:"))
count = 1

def print_name(count,n):

    if count > n:
        return

    print("Priyansh")
    

    print_name(count+1,n)

print_name(count,n)



# 2: print linearly from 1 to n

n = int(input("Enter a number:"))

count = 1

def print_linearly():
    global count

    if count == n:
        return

    print(count)
    count+=1

    print_linearly()

print_linearly()

''' optimal solution: '''
n = int(input("Enter a number:"))

count = 1

def print_linearly(count,n):

    if count > n:
        return

    print(count)
    
    print_linearly(count+1,n)

print_linearly(count,n)



# 3. print linearly from n to 1

n = int(input("Enter a value:"))
count = n

def print_rev():
    global count

    if count < 1: 
        return

    print(count)
    count-=1

    print_rev()

print_rev()

'''optimal solution '''
n = int(input("Enter a value:"))
count = n

def print_rev(count,n):

    if count < 1:
        return

    print(count)
    
    print_rev(count-1,n)

print_rev(count,n)


# 4. print linearly from 1 to n (but by backtraking)

n = int(input("Enter a number:"))
i = n

def back_tacking_using(i,n):

    if i<1:
        return

    back_tacking_using(i-1,n)
    print(i)

back_tacking_using(i,n)

5.

n = int(input("Enter a number:"))
i = n

def second_function(i,n):
    if i<1:
        return

    print(i)

second_function(i-1,n)

second_function(i,n)


'''option way to solve: '''

def backtrack(i,n):

    if i>n:
        return
    
    backtrack(i+1,n)
    print(i)

backtrack(1,5)

