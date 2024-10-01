"""   2-obtenir le dernier mot de la ligne  """
ligne = "La Cigale, ayant chantés"

son = "és"
dico = {"é","er","ez","ey","ai","è","és"}

""" parcourir à l'envers pour extraire le minimum de lettre qui fait un son"""

for i in range(len(ligne)-1,0,-1):
    print(ligne[i])
""" ajouter dans la liste rimes.append(e)   """