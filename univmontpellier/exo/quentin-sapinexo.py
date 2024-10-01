HauteurSapin=int(input("Hauteur du sapin :"))
x = ((HauteurSapin)*2)-1
y = None

for i in range(HauteurSapin):
    y = ((i+1)*2)-1
    print(" "*round((x-y)/2)+"*"*y)

print(" "*(HauteurSapin-1)+"*")
print(" "*(HauteurSapin-1)+"*")