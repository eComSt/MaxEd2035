from tkinter import *

# создаем и настраиваем главное окно
window = Tk()
window.geometry('700x500')
window.title('Анкета')

label = Label(text='Расскажите о себе', font=('Arial', 30))
label.place(x=200, y=10)

about = Message(text='''Мы рады приветствовать вас в нашей анкете дружбы! Пожалуйста, отвечайте на вопросы честно, вся информация останется между нами.''', font=('Arial', 20), width=680)
about.configure(justify=CENTER)
about.place(x=5, y=70)

name = Entry(width=50)
name.place(x=70, y=150)

# создаем и размещаем подпись для поля ввода
label_name = Label(text='ФИО: ', font=('Arial', 15))
label_name.place(x=5, y=150)

# создаем IntVar() для объединения радиокнопок в одну группу
selected = IntVar()
# создаем и размещаем радиокнопки для возможности указания пола 
rad1 = Radiobutton(text='Мужской', value=1, variable=selected) 
rad2 = Radiobutton(text='Женский', value=2, variable=selected)
rad1.place(x=10, y=200)
rad2.place(x=100, y=200) 

# создаем и размещаем виджет для указания возраста
age = Spinbox(from_=0, to=200, width=20)
age.place(x=10, y=300)

check_state = IntVar()                                         check_bnt = Checkbutton(text='Запомнить меня', variable=check_state) 
check_bnt.place(x=10, y=350)
# запускаем цикл обработки событий
window.mainloop() 
