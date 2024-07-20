from tkinter import *
from random import choice

class Game:
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0
        self.moves = ['Камень', 'Ножницы', 'Бумага']
    def move_result(self, user_choice):
        comp_choice = choice(self.moves)
        if user_choice == comp_choice:
            self.draw += 1
            return f'Ход игрока: {user_choice}\nХод компьютера:  {comp_choice}\nНичья'
        elif (user_choice == 'Камень' and comp_choice == 'Ножницы' or
            user_choice == 'Ножницы' and comp_choice == 'Бумага' or
            user_choice == 'Бумага' and comp_choice == 'Камень'):
            self.win += 1
            return f'Ход игрока: {user_choice}\nХод компьютера:  {comp_choice}\nПобеда'
        else:
            self.lose += 1
            return f'Ход игрока: {user_choice}\nХод компьютера:  {comp_choice}\nПоражение'
        
    def show_result(self):
        return f'Выигрыш: {self.win}\nПоражение: {self.lose}\nНичья: {self.draw}'


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x300')
        self.window.title('Камень, ножницы, бумага')
        self.game = Game()
        self.startUI(self.window)
        self.window.mainloop()

    def click(self,user_choice):
        self.lbl['text'] = self.game.move_result(user_choice)
        self.lbl2['text'] = self.game.show_result()
    def startUI(self, window):
        for c in range(3): window.columnconfigure(index=c, weight=1)
        for r in range(3): window.rowconfigure(index=r, weight=1)
        self.btn1 = Button(window, text='Камень', command = lambda: self.click('Камень'))
        self.btn2 = Button(window, text='Ножницы', command = lambda: self.click('Ножницы'))
        self.btn3 = Button(window, text='Бумага', command = lambda: self.click('Бумага'))
        self.btn1.grid(row=2, column=0)
        self.btn2.grid(row=2, column=1)
        self.btn3.grid(row=2, column=2)
        self.lbl = Label(window, text='Игра началась!',font = ('Arial', 20))
        self.lbl.grid(row=1, column=0, columnspan=3)
        self.lbl2 = Label(window, text=self.game.show_result(),font=('Arial', 12))
        self.lbl2.grid(row=0, column=0)

x = GUI()