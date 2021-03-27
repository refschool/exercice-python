# https://dbader.org/blog/python-dunder-methods
import time

bar = [
    " Patientez",
    " atientez ",
    " tientez  ",
    " ientez   ",
    " entez    ",
    " ntez     ",
    " tez      ",
    " ez       ",
    " z        ",
    "          ",
    "         P",
    "        Pa",
    "       Pat",
    "      Pati",
    "     Patie",
    "    Patien",
    "   Patient",
    "  Patiente",

]
i = 0

while True:
    print(bar[i % len(bar)], end="\r")
    time.sleep(.2)
    i += 1
