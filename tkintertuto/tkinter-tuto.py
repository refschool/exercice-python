from tkinter import Tk, Label,Button,Entry, END

window = Tk()


button = Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
formulaire = Entry(fg="black", bg="white", width=50)
def handle_click(event):
    print(event)


button.bind("<Button-1>",handle_click)
button.pack()
formulaire.pack()
window.mainloop()