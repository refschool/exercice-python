from random import randrange

file_client = [1,2,3,4,5,6,7,8,9,10]
duree_totale = 0


while len(file_client) != 0:
    """ code a exécuter tant que ..."""
    duree_totale = duree_totale + randrange(3,10)
    """ enlever un client de file_client """
    file_client.pop()

print(file_client)
print(duree_totale)