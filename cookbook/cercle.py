#https://www.youtube.com/watch?v=1Lfv5tUGsn8

"""message = "Area of circle with r = {radius} is {area}"
r=1
a=2

print(message.format(radius=r,area=a))"""

from math import pi

def circle_area(r):
    if type(r) not in [int,float]:
        raise TypeError("Radius should be either non negative int or float")
    if(r < 0):
        raise ValueError("Value must not be negative")
    return pi * (r**2)


