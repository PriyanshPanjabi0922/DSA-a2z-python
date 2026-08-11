n= int(input("Enter a number:"))

### start this ==> date:23/07/2026

for i in range(n+1):
    for j in range(n):
        print("*",end=" ")
    print()

### ---------------------------------------------------------

for i in range(n+1):
    for j in range(i):
        print("*",end= " ")
    print()

### ---------------------------------------------------------

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

### ---------------------------------------------------------

for i in range(n+1):
    for j in range(i+1):
        print(i,end=" ")
    print()

### ---------------------------------------------------------

space = 0

for i in range(1,n+1):
    for j in range(1,(n+1)-i+1):
        print("* ",end="")
    print()

### ---------------------------------------------------------

for i in range(1,n+1):
    for j in range(1,(n+1)-i+1):
        print(j,end="")
    print()

### ---------------------------------------------------------

for i in range(n):

    # space
    for j in range(n-i-1):
        print(" ",end=" ")

    # star

    for j in range(2*i+1):
        print("*",end=" ")

    # space
    for j in range(n-i-1):
        print(" ",end=" ")
    print()

### ---------------------------------------------------------

for i in range(n):

    # space

    for j in range(i):
        print(" ",end=" ")

    # star

    for j in range(2*n - (2*i+1)):
        print("*",end=" ")

    # space

    for j in range(i):
        print(" ",end=" ")

    print()

### ---------------------------------------------------------

# # the below is already a pattrn not any mistake!

for i in range(n):

    # space
    for j in range(n-i-1):
        print(" ",end=" ")

    # star

    for j in range(2*i+1):
        print("*",end=" ")

    # space
    for j in range(n-i-1):
        print(" ",end=" ")
    print()

for i in range(n):

    # space

    for j in range(i):
        print(" ",end=" ")

    # star

    for j in range(2*n - (2*i+1)):
        print("*",end=" ")

    # space

    for j in range(i):
        print(" ",end=" ")

    print()

### ---------------------------------------------------------


for i in range(1,2*n):
    star = i

    if i>=n:
        star = 2*n-i

    for j in range(0,star):
        print("*",end=" ")
    print()

### ---------------------------------------------------------

start =1
for i in range(0,n):

    if i%2==0:
        start = 1
    else:
        start = 0

    for j in range(0,i+1):
        print(start,end=" ")
        start = 1- start

    print()


space = 2*(n-1)
for i in range(1,n+1):
    

    # number
    for j in range(1,i+1):
        print(j,end="")

    # spaces

    for j in range(1,space+1):
        print(" ",end="")

    # number
    for j in range(i,0,-1):
        print(j,end="")

    print()
    space-=2


### ---------------------------------------------------------
        
num= 1
for i in  range(1,n+1):
    
    for j in range(1,i+1):
        print(num,end=" ")

        num+=1

    print()

### ---------------------------------------------------------

for i in range(1,n+1):
    _char = "A"
    for j in range(1,i+1):
        print(_char,end=" ")
        _char = chr(ord(_char)+1)
    print()


### ---------------------------------------------------------

for i in range(1,n+1):
    _char = "A"
    for j in range(1,n-i+2):
        print(_char,end=" ")
        _char = chr(ord(_char)+1)

    print()


### ---------------------------------------------------------

_char = "A"
for i in range(1,n+1):
    
    for j in range(1,i+1):
        print(_char,end=" ")
    _char = chr(ord(_char)+1)
    print()

### ---------------------------------------------------------


for i in range(n):
    _char = "A"

    # spaces
    for j in range(n-i-1):
        print(" ",end=" ")

    # alphabets 
    breakpoint = int((2*i+1) / 2)
    for j in range(2*i+1):
        print(_char,end=" ")
        if j < breakpoint:
            _char = chr(ord(_char)+1)
        else:
            _char = chr(ord(_char)-1)

    # spaces
    for j in range(n-i-1):
        print(" ",end=" ")

    print()


### ---------------------------------------------------------

for i in range(1,n+1):
    _char = "E"
    for j in range(1,i+1):
        print(_char,end=" ")
        _char = chr(ord(_char)-1)
    print()


### ---------------------------------------------------------

spaces  =0
for i in range(1,n+1):

    # star

    for j in range(1,n-i+2):
        print("*",end=" ")

    # spaces

    for j in range(spaces):
        print(" ",end=" ")

    # star

    for j in range(1,n-i+2):
        print("*",end=" ")

    spaces+=2
    print()

spaces = 2*n-2

for i in range(1,n+1):
    # star

    for j in range(1,i+1):
        print("*",end=" ")

    # spaces

    for j in range(spaces):
        print(" ",end=" ")
    
    # star

    for j in range(1,i+1):
        print("*",end=" ")

    spaces-=2
    print()


### ---------------------------------------------------------

spaces = 2*n-2
for i in range(1,2*n):
    stars = i

    if i>n:
        stars = 2*n-i

    # stars

    for j in range(1,stars+1):
        print("*",end=" ")

    # spaces

    for j in range(1,spaces+1):
        print(" ",end=" ")

    # star

    for j in range(1,stars+1):
        print("*",end=" ")

    print()

    if i<n:
        spaces -=2
    else:
        spaces +=2

### ---------------------------------------------------------

for i in range(n):

    for j in range(n):
        if i==0 or j==0 or i == n-1 or j == n-1:
            print("*",end=" ")
        else:
            print(" ",end=" " )

    print()

# ### ---------------------------------------------------------

for i in range(2*n-1):
    for j in range(2*n-1):

        top = i
        left = j
        right = (2*n -2) - j
        down = (2*n -2) - i

        minDistance = min(top,left,right,down)

        print(n - minDistance ,end=" ")
    print()
