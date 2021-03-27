#convertisseur d'unité
def is_float(string):
    try:
        return float(string)
    except ValueError:
        return False

print(is_float("1.86"))

"""one = 1
two = 2
one,two = two,one
print(one)
print(isinstance("1.86", float) )"""