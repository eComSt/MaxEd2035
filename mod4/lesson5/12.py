import telebot 
TOKEN = '7193230705:AAE-atOL19XgDs1AUakruyRPSN5XgiABV6s' 
bot = telebot.TeleBot(TOKEN) 
smss = [] 
@bot.message_handler(content_types=['text']) 
def echo(message): 
    smss.append(message.text) 
    bot.reply_to(message, message.text) 
bot.infinity_polling()