from tkinter import *
from random import choice,randint
def press():
    colors = ['red','green','blue']
    btn.config(bg=choice(colors))
    btn.place(x=randint(0,300),y=randint(0,300))
window = Tk()
window.title("My Window")
window.geometry(f"400x400+400+400")
btn = Button(text='Click me', font=('Arial', 20), command = press)
btn.place(x=100, y=100)
window.mainloop()