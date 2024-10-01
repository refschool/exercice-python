# conversion de longueur avec paquet ou module
def convert_cm_to_m(long):
    return long / 100

def convert_m_to_cm(long):
    return long * 100

def is_float(long):
    try:
        float(long)
        return True
    except:
        return False

unite = ''
long = ''

while unite not in ['m','cm']:
    unite = input("Entrez l'unité cm ou m: ")

while not is_float(long):
    long = input("Entrez la longueur :")

long = float(long)

if unite == 'm':
    long = convert_m_to_cm(long)
else:
    long = convert_cm_to_m(long)

print(round(long,2))