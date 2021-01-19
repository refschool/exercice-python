#emoji
# import emoji from emojize
"""if result < 0:
    print("\U0001F976")
elif result>35:
    print("\U0001F975")
else:
    print('')"""


# util.py
import os
def C_to_F(tempC):
    tempF = 9 / 5 * tempC + 32
    return tempF

def F_to_C(tempF):
    tempC = (tempF - 32) * 5/9
    return tempC


while(True):
    unit = input('Unité source')
    if(unit not in ['C','F']): # ['C','F'].count(unit),
        break
    temp = int(input ('température'))
    if(unit == 'C'):
        print(C_to_F(temp), ' degré °F')
    else:
        print(F_to_C(temp), ' degré °C')

print('Fin du programme')
