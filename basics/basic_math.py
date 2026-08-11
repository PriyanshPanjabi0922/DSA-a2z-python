import math
num = 5412

def count(num):
    cnt = 0

    while num>0:
        cnt+=1
        num = int(num/10)

    return cnt

print(count(5412))

### ===================================================================

n = 23145
def reverse_number(n):

    res_number = 0

    while n>0:
        last_digit = n % 10
        res_number = (res_number*10) + last_digit

        n = n// 10

    return res_number

print(reverse_number(n))
   
### ===================================================================

n = 123444321

def check_palidrom(n):

    org = n
    res_number = 0

    while n>0:
        last_digit = n % 10
        res_number = res_number*10+last_digit
        n = n//10

    return org == res_number

print(check_palidrom(n))

### ===================================================================

n = 371
def check_armstrong(n):
    armstrong_sum =0 

    org = n

    while n>0:
        last_digit = n% 10
        sum= sum + (last_digit**3)
        n = n // 10

    return org == armstrong_sum

print(check_armstrong(n))

### ===================================================================

### print all divisor!

n = int(input("Enter  a number:"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)

''' optimla solution to this problem'''

divisor_list =[]
n = int(input("Enter  a number:"))
sqare_root = int(n**0.5)
for i in range(1,sqare_root):
    if n%i == 0:
        divisor_list.append(i)
        if n/i != i:
            divisor_list.append(int(n/i))

divisor_list.sort()
print(divisor_list)

### ===================================================================

### Check for prime

# Bruter forse aaproch 

n = int(input("enter a number:"))

counter =0 

for i in range(1,n+1):

    if n%i == 0:
        counter+=1

if counter == 2:
    print("prime number")
else:
    print("not a prime number!")


### optimal appoch:

n = int(input("enter a number:"))

counter =0 

sqare_root = int(n**0.5)

for i in range(1,sqare_root+1):

    if n%i == 0:
        counter+=1
        if (n/i) != i:
            counter +=1

if counter == 2:
    print("prime number")
else:
    print("not a prime number!")


### ===================================================================

### GCD / HCF

#  appling using the bruter forus

n1 = int(input("Enter Value of n1:"))
n2 = int(input("Enter Value of n2:"))

for i in range(min(n1,n2),0,-1):
    if n1%i == 0 and n2%i == 0:
        
        print(i)
        break
    
while n1 > 0 and n2 >0:
    if n1>n2:
        n1= n1%n2
    else:
        n2 = n2%n1

if n1 ==0:
    print(n2)
else:
    print(n1)
        

