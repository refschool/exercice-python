import tkinter

fenetre = tkinter.Tk()

"""   le menu   """
menubar = tkinter.Menu(fenetre)

fenetre.geometry("640x400")
filemenu = tkinter.Menu(menubar)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")
menubar.add_cascade(label="Fichier", menu=filemenu)
fenetre.config(menu=menubar)
"""   fin du menu   """


fenetre.title("Mon application")
entry = tkinter.Entry(fg="black", bg="white", width=50)
entry.pack()
button = tkinter.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.pack()
fenetre.mainloop()