people = [
{'name': "Tom", 'age': 10},
{'name': "Mark", 'age': 5},
{'name': "Pam", 'age': 7}
]

r = filter(lambda person: person['name'] == 'Pam', people)
s= [x for x in people if x['name'] == "Pam"]
print(s[0])

t= [x for x in people if x['name'] == "Pam"]
