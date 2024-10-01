import json
"""
préserver les tuples en json il faut encoder manuellement
https://stackoverflow.com/questions/15721363/preserve-python-tuples-with-json
"""
# Data to be written
""" attention le tuple est tanscodé en liste pendant l'écriture (en fait on n'a pas besoin de tuple à vrai dire...)"""
""" cet exo peut montrer l'intérêt d'avoir des fonction pour avoir un code plus lisible
fonction pour filtrer les valeurs depuis input """
round = {
    "id":1,
    "list_match":[
        {
            "id_match":1,
            "joueur1": {"id":0,"score":0},
            "joueur2":{"id":1,"score":0}
        },
        {
            "id_match":2
            ,"joueur1":{"id":2,"score":0},
            "joueur2":{"id":3,"score":0}
        }
                  ]
}

# Serializing json
json_object = json.dumps(round, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
    # json.dump(yon, outfile)