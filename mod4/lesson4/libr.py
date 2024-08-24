from functools import wraps
import logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s',filename='log.log')
def log(func):
    '''Декоратор, который выводит сообщение перед выполнением функции.'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Вызывается функция: {func.__name__}')
        logging.info(f'Документация: {func.__doc__}')
        return func(*args, **kwargs)
    return wrapper

#Debug
#Info
#Warning
#Error
#Critical

books = {}

@log
def add_book(title, author):
    '''Добавляет книгу с указанным названием и автором в каталог.'''
    if title not in books:
        books[title] = author
        print(f'Книга {title} автора {author} успешно добавлена в каталог.')
    else:
        print(f'Книга {title} уже есть в каталоге.')

@log
def find_book(title):
    '''Ищет книгу по названию и возвращает статус наличия в каталоге.'''
    if title in books:
        print(f'Книга {title} найдена в каталоге.')
    else:
        print(f'Книга {title} отсутствует в каталоге.')


while True:
    command = input('Введите команду: ').lower()
    if command == 'exit':
        break
    elif command == 'add':
        title = input('Введите название книги: ')
        author = input('Введите автора книги: ')
        add_book(title, author)
    elif command == 'find':
        title = input('Введите название книги: ')
        find_book(title)
    else:
        print('Неизвестная команда.')