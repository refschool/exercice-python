


def get_recursive_factorial(n):
    if n < 2 :
        return 1
    else:
        return n * get_recursive_factorial(n-1)

fac =  get_recursive_factorial(5)

print(fac)