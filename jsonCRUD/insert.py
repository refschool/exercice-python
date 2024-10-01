import json
"""
préserver les tuples en json il faut encoder manuellement
https://stackoverflow.com/questions/15721363/preserve-python-tuples-with-json
"""
# Data to be written
""" attention le tuple est tanscodé en liste pendant l'écriture (en fait on n'a pas besoin de tuple à vrai dire...)"""
round = {
    "id":1,
    "list_match":[([0,0],[1,0]),
                  ([2,0],[3,0]),
                  ]
}

# Serializing json
json_object = json.dumps(round, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
    # json.dump(yon, outfile)