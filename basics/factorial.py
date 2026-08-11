''' PROGRAM FOR PRINTING FIRST NATURAL NUMBERS: '''

## parameterize:

n = int(input("Enter the nature number you want to calculate the sum:"))
sum =0

def natural_no_parameter(n,sum):

    if n < 1:
        print(sum)
        return
    natural_no_parameter(n-1,sum+n)

natural_no_parameter(n,sum)

## function:

n = int(input("Enter a number:"))

def natural_number(n):

    if n == 0:
        return 0

    return n + natural_number(n-1)

print(natural_number(n))

## FACTORIAL PROGRAM:

n = int(input("Enter the number:"))

def factorial_recursion(n):
    if n == 1:
        return 1

    return n * factorial_recursion(n-1)

print(factorial_recursion(n))

