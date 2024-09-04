import telebot
import os
from dotenv import load_dotenv
from api import *

load_dotenv()
TOKEN = os.getenv("TOKEN")
print(TOKEN)
bot = telebot.TeleBot(TOKEN)

USERS = {}

@bot.message_handler(commands=["start"])
def start(message):
    mes = 'Добрый день! Я бот, показывающий прогноз погоды.'
    bot.send_message(message.chat.id, mes)
    change_city(message)


def change_city(message):
    mes = 'Введите город'
    bot.send_message(message.chat.id, mes)
    bot.register_next_step_handler(message, save_city)


def save_city(message):
    USERS[message.chat.id] = message.text
    mes = f'Город {message.text} успешно сохранен!'
    bot.send_message(message.chat.id, mes, reply_markup=menu())


def menu():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3, 
                                               resize_keyboard=True,
                                               one_time_keyboard=False)
    but1 = telebot.types.KeyboardButton('Текущая погода')
    but2 = telebot.types.KeyboardButton('Подробный прогноз на дату')
    but3 = telebot.types.KeyboardButton('Сменить город')
    markup.add(but1, but2, but3)
    return markup


def current_weather(message):
    city = USERS[message.chat.id]
    try:
        mes = get_weather(city)
    except:
        mes = 'Не удалось получить данные о погоде в вашем городе'
    bot.send_message(message.chat.id, mes)


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Текущая погода':
       current_weather(message)
    elif message.text == 'Подробный прогноз на дату':
        bot.reply_to(message, 'Данная функция находится в разработке')
    elif message.text == 'Сменить город':
        change_city(message)
    else:
        bot.reply_to(message, 'Неизвестная команда')

bot.infinity_polling()