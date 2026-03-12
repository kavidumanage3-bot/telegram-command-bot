import telebot

TOKEN = "8799375203:AAEbldBCM66UiShErsHzHxRO9nejgot7kO0"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome to my bot!")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Commands:\n/start\n/help")

@bot.message_handler(commands=['topup'])
def topup(message):
    bot.reply_to(message, "💰 Topup service available!")

bot.infinity_polling()
