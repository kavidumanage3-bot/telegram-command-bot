import telebot

TOKEN = "8799375203:AAEbldBCM66UiShErsHzHxRO9nejgot7kO0"  # <-- මෙතන BotFather token එක

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome to my bot!")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Commands:\n/start\n/help\n/topup")

@bot.message_handler(commands=['topup'])
def topup(message):
    bot.reply_to(message, "💰 Topup service available!")

# Bot run
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
