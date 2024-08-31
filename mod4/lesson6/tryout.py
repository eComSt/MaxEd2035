import telebot

bot = telebot.TeleBot("7193230705:AAE-atOL19XgDs1AUakruyRPSN5XgiABV6s")

@bot.message_handler(commands=["start"])
def start(message):
    mess = f"Привет, {message.from_user.first_name} {message.from_user.last_name}"
    bot.send_message(message.chat.id, mess, parse_mode="html")

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode="html")
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode="html")
    elif message.text == "photo":
        try:
            with open("/Users/pattycha/MaxEd2035-1/mod4/lesson6/images.jpeg", "rb") as photo:
                bot.send_photo(message.chat.id, photo)
        except FileNotFoundError:
            bot.send_message(message.chat.id, "Изображение не найдено", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode="html")



bot.polling(none_stop=True)