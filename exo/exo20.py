tmp = 3


def test():
    global tmp
    tmp = 5
    print(tmp)

def add(a,b):
    #global tmp
    tmp = a + b

def modulo(c):
    return tmp % c

#print(tmp)
#print(modulo(5))
print('tmp = ',tmp)
test()
print('tmp = ',tmp)
