import requests
import telebot

# -----------------------------
# Telegram Bot setup
# -----------------------------
BOT_TOKEN = "8799375203:AAEbldBCM66UiShErsHzHxRO9nejgot7kO0"
bot = telebot.TeleBot(BOT_TOKEN)

# Example chat_id (web order notify)
WEB_CHAT_ID = "8324590734"

# -----------------------------
# Command Handlers
# -----------------------------
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "👋 Welcome to Order Bot!")

@bot.message_handler(commands=['help'])
def help_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Commands:\n/start\n/help\n/topup\n/orders")

@bot.message_handler(commands=['topup'])
def topup(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "💰 Topup service available!")

@bot.message_handler(commands=['orders'])
def orders(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "🛒 Send web orders to this bot automatically!")

# -----------------------------
# Function to send web order to Telegram
# -----------------------------
def send_web_order(customer_name, amount):
    message = f"🛒 New Order Received!\nCustomer: {customer_name}\nAmount: ${amount}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": WEB_CHAT_ID,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Message sent successfully ✅")
    else:
        print("Failed to send message ❌", response.text)

# -----------------------------
# Example Web Order Call
# -----------------------------
send_web_order("John Doe", 10)

# -----------------------------
# Run bot
# -----------------------------
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
