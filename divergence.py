import openpyxl
import pandas as pd

path = "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\divergence.xlsx"
df = pd.read_excel(path,engine="openpyxl")
print(df.head())

print(df.describe())

'''
path = "C:\\Users\\Admin\\PycharmProjects\\pythonProject\\divergence.xlsx"
wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active
cell_obj = sheet_obj.cell(row = 2, column = 6)

print(cell_obj.value)


'''
