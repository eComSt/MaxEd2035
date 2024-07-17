from tkinter import *

window = Tk()
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
print(w,h)
window.title("My Window")
window.geometry(f"{int(w/2)}x{int(h/2)}+400+700")

window.mainloop()