st = {
    "Ромео и Джульетта": "Шекспир",
    "Бойцовский клуб": "Чак Паланик",
    "Таня Гроттер": "Дмитрий Емец",
}
print('Список возможных действий:')
print('1 - Добавить новую книгу')
print('2 - Поиск книги по названию')
print('3 - Удаление книги из каталога')
print('4 - Показать информацию о всех книгах в каталоге')
print('0 - Закончить работу')
number=int(input("Введите число: "))
while number!= 0:
    if number==1:
        title = input('Введите название книги:')
        while title in st:
            title = input('Такая книга уже есть, введите другое название')
        author = input('Введите имя автора:') 
        st[title] = author
    elif number==2:
        title = input('Введите название книги:')
        if title in st:
            print(f'Автор книги {title} - {st[title]}')
        else:
            print('Книга не найдена')
    elif number==3:
        title = input('Введите название книги:')
        if title in st:
            del st[title]
            print(f'Книга {title} удалена')
        else:
            print('Книга не найдена')
    elif number==4:
        for title, author in st.items():
            print(f'Книга {title} - {author}')
    else:
        print('Неверное действие. Попробуйте еще раз.')
    number=int(input("Введите число: "))
print('--------------------------------------------------------------')
print('Спасибо за использование программы!')