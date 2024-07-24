from customtkinter import *
def click():
    global counter
    counter += 1
    clicks.configure(text = f"Количество нажатий: {counter}")
window = CTk()
window.geometry("300x300")
window.title("CustomTkinter")
window.grid_columnconfigure(index = (0), weight=1)
window.grid_rowconfigure(index = (0,1,2,3), weight=1)
label = CTkLabel(window, text="Hello World")
label.grid(row = 0, column = 0)
label.cget('font').configure(size=40)
counter = 0
clicks = CTkLabel(window, text = f"Количество нажатий{counter}")
clicks.grid(row = 1, column = 0)
button = CTkButton(window, text = "Нажми меня", fg_color="blue", command = click)
button.grid(row = 2, column = 0)
fr = CTkFrame(window)
fr.grid_columnconfigure(index = (0), weight=1)
fr.grid_rowconfigure(index = (0,1), weight=1)
fr.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nsew")
checkbox_1 = CTkCheckBox(fr, text = "Первый чекбокс")
checkbox_1.grid(row = 0, column = 0)
checkbox_2 = CTkCheckBox(fr, text = "Второй чекбокс")
checkbox_2.grid(row = 1, column = 0)
window.mainloop()