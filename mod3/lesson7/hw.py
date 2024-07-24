from customtkinter import *
from random import randint
def click():
    user_data = v.get()
    global r
    if user_data == r:
        r = randint(1,3)
        label.configure(text = f"Отлично!  нажми {r}")
    else:
        label.configure(text = f"Неверно!  нажми {r}")
r = randint(1,3)
window = CTk()
window.geometry("300x300")
window.title("CustomTkinter")
window.grid_columnconfigure(index = (0,1,2), weight=1)
window.grid_rowconfigure(index = (0,1,2), weight=1)
label = CTkLabel(window, text=f"Нажми {r}")
label.grid(row = 0, column = 0)
label.cget('font').configure(size=40)
fr = CTkFrame(window)
fr.grid_columnconfigure(index = (0,1,2), weight=1)
fr.grid_rowconfigure(index = (0), weight=1)
fr.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "nsew")
v = IntVar()
checkbox_1 = CTkRadioButton(fr, text = "Кнопка 1", variable=v, value=1)
checkbox_1.grid(row = 0, column = 0)
checkbox_1 = CTkRadioButton(fr, text = "Кнопка 2", variable=v, value=2)
checkbox_1.grid(row = 0, column = 1)
checkbox_1 = CTkRadioButton(fr, text = "Кнопка 3", variable=v, value=3)
checkbox_1.grid(row = 0, column = 2)
button = CTkButton(window, text = "Проверить", command = click)
button.grid(row = 2, column = 0, sticky = "ew")
window.mainloop()