# Работа с Custom Tkinter I

# Программа "Анкета"

# Графический интерфейс состоит из следующих частей:
# 1) Главное окно со всеми виджетами
# 2) Группа чекбоксов для выбора цвета (Красный, Синий, Зеленый)
# 3) Группа радиокнопок для выбора фигур (Круг, Квадрат)
# 4) Стандартная кнопка для отправки значений с чекбоксов и радиокнопки
# 5) Область с текстом для отображения значений с выбранных чекбоксов и радиокнопки

# Код приложения состоит из 3-х классов:
# 1) MainWindow - главное окно, на котором располагаются все виджеты
# 2) MyCheckboxFrame - фрейм с чекбоксами 
# 3) MyRadiobuttonFrame - фрейм с радиокнопками 

from customtkinter import *

# класс для главного окна
class MainWindow(CTk):
    # инициализатор класса
    def __init__(self):
        # вызываем инициализатор из родительского класса
        super().__init__()
        # задаем название и размеры главного окна
        self.title('Цвета и фигуры')
        self.geometry('400x300')
        # задаем сеточную конфигурацию 
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        # создаем и размещаем стандартную кнопку
        self.button = CTkButton(self, text='Отправить', command=self.show_info)
        self.button.grid(row=1, padx=10, pady=10, sticky='ew', columnspan=2)
        # создаем и размещаем лейбл с данными из чекбоксов и радиокнопок
        self.text = CTkLabel(self, text='')
        self.text.grid(row=2, padx=10, pady=10, sticky='ew', columnspan=2)
        # создаем и размещаем фрейм с чекбоксами
        self.checkbox_frame = MyCheckboxFrame(self, title='Выбери цвет', values=('Красный', 'Синий', 'Зеленый'))
        self.checkbox_frame.grid(row=0, column=0,  padx=10, pady=10, sticky='nsew')
        # создаем и размещаем фрейм с радиокнопками
        self.radiobutton_frame = MyRadiobuttonFrame(self, title='Выбери фигуру', values=('Круг', 'Квадрат'))
        self.radiobutton_frame.grid(row=0, column=1,  padx=10, pady=10, sticky='nsew')

    # метод для отображения данных с чекбоксов и радиокнопок
    def show_info(self):
        self.text.configure(text=f'Цвета: {self.checkbox_frame.get()}\n Фигура: {self.radiobutton_frame.get()}')

# класс фрейма с чекбоксами
class MyCheckboxFrame(CTkFrame):
    # инициализатор класса
    def __init__(self, master, title, values):
        # вызываем инициализатор из родительского класса
        super().__init__(master)
        # задаем сеточную конфигурацию
        self.grid_columnconfigure(0, weight=1)
        # список для хранения чекбоксов
        self.checkboxes = []
        # создаем и размещаем лейбл с названием группы чекбоксов
        self.title = CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        # цикл для передачи названий цветов в чекбоксы
        for i in range(len(values)):
            # создаем и размещаем чекбоксы с переданными названиями цветов
            checkbox = CTkCheckBox(self, text=values[i])
            checkbox.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")
            # добавляем созданный чекбокс в список
            self.checkboxes.append(checkbox)

    # метод для получения данных из чекбоксов
    def get(self):
        # список для хранения цветов из выбранных чекбоксов
        checked_checkboxes = []
        # цикл для прохода по списку с чебоксами
        for checkbox in self.checkboxes:
            # если чекбокс выбран
            if checkbox.get() == 1:
                # сохраняем значение (цвет) в список
                checked_checkboxes.append(checkbox.cget("text"))
        # возвращаем список с выбранными цветами
        return ', '.join(checked_checkboxes)
    
# клаcc фрейма с радиокнопками
class MyRadiobuttonFrame(CTkFrame):
    # инициализатор класса
    def __init__(self, master, title, values):
        # вызываем инициализатор из родительского класса
        super().__init__(master)
        # задаем сеточную конфигурацию
        self.grid_columnconfigure(0, weight=1)
        # строковый объект для сохранения выбранной фигуры
        self.figure = StringVar()
        # создаем и размещаем лейбл с названием группы чекбоксов 
        self.title = CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        # цикл для передачи названий фигур в радиокнопки
        for i in range(len(values)):
            # создаем и размещаем чекбоксы с переданными названиями фигур
            radiobutton = CTkRadioButton(self, text=values[i], value=values[i], variable=self.figure)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")

    # метод для получения данных из радиокнопок
    def get(self):
        return self.figure.get()

# создаем главное окно со всеми виджетами
window = MainWindow()
# запускаем цикл обработки событий
window.mainloop()
