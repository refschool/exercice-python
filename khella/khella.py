from pprint import pprint
Xmax = 16
Ymax = 9

rect = ((-3, 7), 3, 2)

def coupe(r):
    """ Rect -> Rect """
    p,l,c = r
    lp,cp = p
    if(cp<0 or cp>=16 or lp<0 or lp>=9):
        return ((0,0),0,0)
    else:
        #print(l,9-lp)
        return (p, min(l, 9-lp), min(c, 16-cp))




def pixel(rect):
    rect = coupe(rect)
    s = set()
    (lp,cp),ligne,col = rect
    for l in range(0,ligne):
        for c in range(0,col):
            s.add((lp + l,cp + c ))
    return s

"""res = pixel(rect)
print(res)"""


"""def image_blanche():
    l =  [ 0 for _ in range(16)]
    liste2D = [l for i in range(9)]
    return liste2D"""

def image_blanche():
    liste2D = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for i in range(9)]
    return liste2D

liste2D = image_blanche()
liste2D[0]

for el in liste2D:
    print(id(el))

