def convert_cm_to_m(longueur):
    if __name__ == '__main__':
        print("je suis dans le fichier principal, je ne m'exécute pas je suis destiné à être importé")
    else:
        print("je ne suis pas dans le fichier principal je peux fonctionner")
        lg_m = int(longueur) / 100
        return lg_m



def convert_m_to_cm(longueur):
    lg_cm = float(longueur) * 100
    return lg_cm

value = convert_cm_to_m(100)
print(value)
