import csv
with open('annuaire.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    linecount = 0
    for row in csvreader:
        if linecount == 0:
            print(f'{", ".join(row)}')
            linecount += 1
        elif linecount > 10:
            break
        else:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}')
            linecount += 1