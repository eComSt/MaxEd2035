import json
import telebot
from random import choice



TOKEN = "7193230705:AAE-atOL19XgDs1AUakruyRPSN5XgiABV6s"
bot = telebot.TeleBot(TOKEN)

users = json.load(open('users.json'))
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Я бот для переписки!")

@bot.message_handler(commands=['reg'])
def reg(message):
    user = message.from_user.username
    id = message.chat.id
    users[user] = id
    print('USER ADD', user, id)
    json.dump(users, open('users.json', 'w'), indent=4)
    bot.send_message(id,"Вы добавлены в список рассылки")

@bot.message_handler(commands=['del'])
def delete(message):
    user = message.from_user.username
    id = message.chat.id
    if user in users:
        del users[user]
    json.dump(users, open('users.json', 'w'), indent=4)
    bot.send_message(id,"Вы исключены из списка рассылки")

@bot.message_handler(commands=['list'])
def lst(message):
    id = message.chat.id
    bot.send_message(id,'\n'.join(list(users.keys())))

@bot.message_handler(content_types=['text'])
def echo_message(message):
    user = message.from_user.username
    id = message.chat.id
    if user in users:
        # id = users[user]
        # print(id)
        # send = choice(list(users.items()))
        # print(users)
        # print(send)
        bot.send_message(choice(list(users.values())),message.text)
    else:
        bot.send_message(id,"Вы не зарегистрированы!")
bot.infinity_polling()