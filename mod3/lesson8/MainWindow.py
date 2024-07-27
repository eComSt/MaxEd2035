from customtkinter import *
from MyCheckboxFrame import *
from MyRadiobuttonFrame import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.val_check = ['Красный', 'Синий', 'Зеленый']
        self.val_radio = ['Круг', 'Квадрат']
        self.title("Цвета и фигуры")
        self.geometry("400x300")
        # self.resizable(False, False)
        self.__draw()

    def __draw(self):
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.button = CTkButton(self, text="Отправить", command=self.show_info)
        self.button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky = "nsew")

        self.text = CTkLabel(self, text="")
        self.text.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky = "nsew")

        self.checkbox_frame = MyCheckboxFrame(self, title="Выбери цвет", values=self.val_check)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=10, sticky = "nsew")

        self.radio_frame = MyRadiobuttonFrame(self, title="Выбери фигуру", values=self.val_radio)
        self.radio_frame.grid(row=0, column=1, padx=10, pady=10, sticky = "nsew")

    def show_info(self):
        self.text.configure(text=f"Выбрано цвет: {self.checkbox_frame.get()}\nФигура: {self.radio_frame.get()}")