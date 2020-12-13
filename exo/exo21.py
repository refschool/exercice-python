import csv
liste = [65,14,22,101,10,9,18,71]

max = liste[0]
for x in liste:
    if(max < x):
        max = x

print(max)
