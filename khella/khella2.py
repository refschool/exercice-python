s = "11100111110"

def toto(s):
    y = "0"
    z = 0
    x = []
    for a in s:
        if a == y:
            z = z + 1
        else:
            x.append(z)
            z = 1
            if y == "0":
                y = "1"
            else:
                y = "0"

    x.append(z)
    print(x)

toto(s)