def test(*argv):
    print(type(argv))
    for arg in argv:
        print(arg)

#test('a','b','c',2)


def test2(**kwarg):
    print(type(kwarg))
    for arg in kwarg:
        print(arg)

#test2(prenom = "Yvon",nom="Huynh")


def test3(*argv,**kwargs):
    print(type(kwargs))
    for arg in argv:
        print(arg)
    for arg in kwargs:
        print(arg)

test3('c','d',prenom = "Yvon",nom="Huynh")