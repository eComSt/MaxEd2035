from tkinter import *
from random import randint

class Game:
    def __init__(self):
        self.comp_choice = randint(1,100)
    def move_result(self, user_choice):
        if user_choice == self.comp_choice:
            return 'Вы угадали!'
        elif self.comp_choice > user_choice:
            return 'Мое число больше!'
        else:
           return 'Мое число меньше!'
        

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x300')
        self.window.title('Угадай число')
        self.game = Game()
        self.startUI(self.window)
        self.window.mainloop()

    def click(self,user_choice):
        try:
            user_choice = int(user_choice)
        except:
            self.lbl2['text'] = 'Введите корректное число!'
        if user_choice > 0 and user_choice < 101:
            self.lbl2['text'] = self.game.move_result(user_choice)
        else:
            self.lbl2['text'] = 'Введите число от 1 до 100 включительно!'


    def startUI(self, window):
        for r in range(4): window.rowconfigure(index=r, weight=1)
        self.lbl = Label(window, text='Угадай число от 1 до 100 включительно',font = ('Arial', 20))
        self.enter = Entry(window, width=10)
        self.btn1 = Button(window, text='Проверить', command = lambda: self.click(self.enter.get()))
        self.lbl2 = Label(window, text="Введите число от 1 до 100 включительно!", font=('Arial', 12))
        self.lbl.grid(row=0, column=0)
        self.enter.grid(row=1, column=0)
        self.btn1.grid(row=2, column=0)
        self.lbl2.grid(row=3, column=0)

x = GUI()