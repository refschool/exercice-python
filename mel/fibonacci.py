def fib(n):
    a = 0
    b = 1
    i=0
    total = 0
    while i < n:
        total = a + b
        a=b
        b=total
        i = i + 1
    return total

print(fib(5))




