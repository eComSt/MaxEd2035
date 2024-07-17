from tkinter import *

window = Tk()
window.title("My Window")
window.geometry(f"400x400+400+700")
label = Label(text='Hello', font=('Arial', 20))
label.place(x=0, y=0)
window.mainloop()