import os
import telebot
from random import choice
from dotenv import load_dotenv
from time import sleep
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
smss = []
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard=telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button_1 = telebot.types.KeyboardButton('Привет')
    button_2 = telebot.types.KeyboardButton('Как дела?')
    keyboard.add(button_1, button_2)
    bot.send_message(message.chat.id,"HELLO IM A BOT!",reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Пока что я умею только повторять за вами :)")

@bot.message_handler(content_types=['text'])
def echo_message(message):
    smss.append(message.text)
    if message.text == 'Как дела?':
        bot.reply_to(message, "Хорошо, а у вас?")
    elif message.text == 'Привет':
        bot.reply_to(message, "ПРИВЕТ!")
    else:
        bot.reply_to(message, choice(smss))

bot.infinity_polling()