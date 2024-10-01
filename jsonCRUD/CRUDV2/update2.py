import json

with open("sample.json","r+") as outfile:
    data = json.load(outfile)
    list_match = data['list_match']

    for match in list_match:
        print("="*20)
        print(f"match_id {match['id_match']}")
        """ affichage plus friendly  """
        print(f"id joueur {match['joueur1']['id']} contre id opposant {match['joueur2']['id']} ")
        print(f"Score {match['joueur1']['score']} - {match['joueur2']['score']} ")


    id_match = int(input(f">>Entrez l'id du match à modifier: "))
    """ méthode filter qui retourne un objet filter à convertir en list """
    match = list(filter(lambda x: x['id_match'] == id_match, list_match))
    match = match[0]
    print(f"mise à jour du match {id_match}")
    score_joueur1 = float(input(f"Entrez score joueur {match['joueur1']['id']}: "))
    score_joueur2 = float(input(f"Entrez score joueur {match['joueur2']['id']}: "))
    match['joueur1']['score'] = score_joueur1
    match['joueur2']['score'] = score_joueur2
    """sauvegarde fichier """
    # Serializing json
    json_object = json.dumps(data, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
    # json.dump(yon, outfile)