import pandas as pd
import os
folder = "csv"
fichiers = os.listdir(folder)

i = 0
tmp_files = []
while i < len(fichiers):
    df = pd.read_csv(folder + '/' + fichiers[i])
    tmp_files.append(df)
    i = i+1

finaldf = pd.concat(tmp_files)
finaldf.to_csv('final.csv',index=False)