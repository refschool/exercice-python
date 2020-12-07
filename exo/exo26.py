import csv
with open('test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)