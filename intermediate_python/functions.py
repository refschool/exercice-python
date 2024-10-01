# concatenate list

L1 = [3,2,1]
L2 = [4,5,6]
print(L1 + L2)

#concatenate dictionary

D1 = {"nom":"Dupont"}
D2 = {"prenom":"jules"}

D1.update(D2)
print(D1)

"""# merge operator python 3.9
D3 = D1 | D2
print(D3)"""

""" eliminate duplicate key, if you want to keep dup key, write own function to store value in list for the duplicated key which can appear once in dictionary"""
dict1 = {  'Ritika': 5, 'Sam': 7, 'John' : 10 }
dict2 = {'Aadi': 8,'Sam': 20,'Mark' : 11 }
print({**dict1,**dict2})

# find something in dictionary with get()
print(D1.get('nom'))
print(D1.get('age'))


""" deep copy"""
"""Assignment statements in Python do not create copies of objects, they only bind names to an object. For immutable objects, that usually doesn’t make a difference."""
"""factory functions shallow copy
new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)

"""
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy
xs.append(['new sublist'])
print(xs)
print(ys)
xs[1][0] = 'X'
print(xs)
print(ys)

""" deepcopy"""
import copy
zs = copy.deepcopy(xs)
""" copy.cpy() is shallow, copy.deepcopy() is deep, apply to classe as well 
Making a shallow copy of an object won’t clone child objects
"""

""" bool(param) convertit en booléen"""
print(bool(""))
print(bool(" "))

"""index de tuple """
vowels = ('a', 'e', 'i', 'o', 'i', 'u')
# index of 'e' in vowels
index = vowels.index('e')
index = vowels.index('i')


""" ternary operator """
print('true' if True else 'false')




