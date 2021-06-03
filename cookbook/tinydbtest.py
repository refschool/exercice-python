from tinydb import  TinyDB, Query

db = TinyDB('tinydb.json')
"""db.insert({'fruit':'apple','price':10})
db.insert({'fruit':'orange','price':25})
db.insert({'fruit':'peach','price':15})"""
Ft = Query()
res = db.search(Ft.fruit == 'orange')

db.update({'price':12}, Ft.fruit == 'peach')
all = db.all()
print(all)
db.remove(Ft.price < 13)

all = db.all()
print(all)