## Multiple recusion call:

# fibonacci series :

n = int(input("Enter a number:"))

def fibonacci(n):
    if n<=1:
        return n

    last = fibonacci(n-1)
    secnd_last = fibonacci(n-2)

    return last + secnd_last

print(fibonacci(n))