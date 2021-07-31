import numpy as np
'''https://www.kite.com/python/answers/how-to-sort-the-rows-of-a-numpy-array-by-a-column-in-python'''
'''https://stackoverflow.com/questions/22392497/how-to-add-a-new-row-to-an-empty-numpy-array'''
list1 = ['bitcoin',2,30]
list2 = ['ether',5,13]
list3 = ['bnb',1.2,26]

#a = np.array([list1,list2,list3])

a = np.empty((0,3))
a =np.append(a,np.array([list1]),axis=0)
a =np.append(a,np.array([list2]),axis=0)
a =np.append(a,np.array([list3]),axis=0)
print(a)

''' sort along a column'''
b = a[np.argsort(a[:,2])]

print(a[:,2])
print(np.argsort(a[:,2]))

print(b)
