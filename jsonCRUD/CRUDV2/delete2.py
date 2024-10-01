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


    id_match = int(input(f">>Entrez l'id du match à effacer: "))
    idx = 0
    for match in list_match:
        if(match['id_match'] == id_match):
            break
        idx = idx + 1


    print(f"effacement du match {id_match}")
    del list_match[idx]

    """sauvegarde fichier """
    # Serializing json
    json_object = json.dumps(data, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
    # json.dump(yon, outfile)