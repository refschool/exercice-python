""" exercice : essayer de mémoriser la structure du json et faire de tête """
import json

with open("sample.json","r") as outfile:
    data = json.load(outfile)
    list_match = data['list_match']
    for match in list_match:
        print("="*20)
        print(f"match_id {match['id_match']}")
        """ affichage plus friendly  """
        print(f"id joueur {match['joueur1']['id']} contre id opposant {match['joueur2']['id']} ")
        print(f"Score {match['joueur1']['score']} - {match['joueur2']['score']} ")



    """ technique pour afficher avec les indentation un dico"""
    #pretty = json.dumps(data, indent=4)
    #print(pretty)



