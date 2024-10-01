
import json

with open("sample.json","r") as outfile:
    data = json.load(outfile)
    list_match = data['list_match']
    for i in range(len(list_match)):
        print("="*20)
        print('match_id '+str(i), list_match[i])
        match = list_match[i]
        """ affichage plus friendly  """
        print(f"id joueur {match[0][0]}   contre id opposant {match[1][0]} " )
        print(f"Score {match[0][1]} - {match[1][1]} ")



    """ technique pour afficher avec les indentation un dico"""
    #pretty = json.dumps(data, indent=4)
    #print(pretty)



