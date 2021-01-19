#raise error

def test( a ):
    if(a < 0):
        raise ValueError
    if(a ==0):
        raise TypeError("the type is not good")
    return a

test(0)