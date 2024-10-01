import json

with open("sample.json","r+") as outfile:
    data = json.load(outfile)
    list_match = data['list_match']

    for i in range(len(list_match)):
        print("="*20)
        print('match_id '+str(i), list_match[i])
        match = list_match[i]
        """ affichage plus friendly  """
        print(f"id joueur {match[0][0]}   contre id opposant {match[1][0]} " )
        print(f"Score {match[0][1]} - {match[1][1]} ")


    id_match = int(input(f">>Entrez l'id du match à modifier: "))
    match = list_match[id_match]
    print(f"mise à jour du match {id_match}")
    score_joueur1 = float(input(f"Entrez score joueur {match[0][0]}: "))
    score_joueur2 = float(input(f"Entrez score joueur {match[1][0]}: "))
    match[0][1] = score_joueur1
    match[1][1] = score_joueur2
    """sauvegarde fichier """
    # Serializing json
    json_object = json.dumps(data, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
    # json.dump(yon, outfile)