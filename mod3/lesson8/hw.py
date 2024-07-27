from customtkinter import *

# класс для группы радиокнопок, наследуемся от CTkFrame
class MyRadiobuttonFrame(CTkFrame):
    # инициализатор класса
    def __init__(self, master):
        # вызываем инициализатор из базового класса
        super().__init__(master)
        # настраиваем сеточную конфигурацию
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        # создаем и размещаем подпись 
        self.title = CTkLabel(self, text='Радиокнопки')
        self.title.grid(row=0, column=0, columnspan=1)
        # создаем объект для группировки кнопок
        self.selected = IntVar()
        # создаем и размещаем 3 радиокнопки
        for i in range(1, 4):
            radiobutton = CTkRadioButton(self, text=f'Кнопка {i}', value=i, variable=self.selected)
            radiobutton.grid(row=i, column=0, columnspan=1)

# класс главного окна, наследуемся от CTkFrame
class App(CTk):
    # инициализатор класса
    def __init__(self):
        # вызываем инициализатор из базового класса
        super().__init__()
        # задаем размеры и название окна
        self.geometry('300x200')
        self.title('Главное окно')
        # настраиваем сеточную конфигурацию
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # создаем и размещаем объект с группой радиокнопок
        self.my_frame = MyRadiobuttonFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

# создаем экземпляр класса App
app = App()
# запускаем цикл обработки событий
app.mainloop()
