import telebot

# BotFather token එක දැමන්න
TOKEN = "8799375203:AAEbldBCM66UiShErsHzHxRO9nejgot7kO0"

# Bot object
bot = telebot.TeleBot(TOKEN)

# /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome to my bot!")

# /help command
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Commands:\n/start\n/help\n/topup")

# /topup command
@bot.message_handler(commands=['topup'])
def topup(message):
    bot.reply_to(message, "💰 Topup service available!")

# Run bot
if __name__ == "__main__":
    bot.infinity_polling()
