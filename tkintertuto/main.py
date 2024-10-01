#https://realpython.com/python-gui-tkinter/
from tkinter import Tk, Label,Button,Entry, END
window = Tk()
"""label1 = Label(window, text="Hello, world!")
label1.pack() #reduce to minimum size"""

""" available widgets
Label:display text or image
, Button, Entry, Text,Frame

"""
"""label2 = Label(text="Huynh Yvon", foreground="white",bg="black",width=50,height=10)
label2.pack()"""


def handle_wheel(event):
    """formulaire.insert(0,"click me !")"""
    print(event)



def handle_keypress(event):
    """    print(event.char)"""
    """formulaire.insert(0,"click me !")"""
    #formulaire.delete(0,END)
    print("Vous avez appuyeé sur X")


def handle_click(event):
    """Every Button widget has a command attribute"""
    print(event)
    formulaire.delete(0,END)
    formulaire.insert(0,"Mouse left button clicked")
def handle_right_click(event):
    """Every Button widget has a command attribute"""
    print(event)
    formulaire.delete(0,END)
    formulaire.insert(0,"Mouse right button clicked")

def handle_middle_click(event):
    print(event)
    formulaire.delete(0,END)
    formulaire.insert(0,"Mouse middle button (Wheel) clicked")

button = Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)


formulaire = Entry(fg="black", bg="white", width=50)

button.bind("<Button-1>",handle_click)
button.bind("<Button-2>",handle_middle_click)
button.bind("<Button-3>",handle_right_click)
button.bind("<MouseWheel>",handle_wheel)
window.bind("<Return>",handle_keypress)

button.pack()
formulaire.pack()

formulaire.insert(0, "Programmation ")
formulaire.insert(14, "Python")


window.bind("x",handle_keypress)
window.mainloop()  #run event loop
