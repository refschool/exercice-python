
lambda x: 3*x +1
g = lambda x: 3*x + 1
#print(g(2))

f = lambda x,y:x*x + y*y

#return lambda function


def ellipse(a,b):
    return lambda x, y: a * x**2 + b * y**2

l = ellipse(1,1)
print(l(2,3))