import telebot
import json

BOT_TOKEN = "8799375203:AAEbldBCM66UiShErsHzHxRO9nejgot7kO0"
bot = telebot.TeleBot(BOT_TOKEN)

# Simple in-memory database (replace with real DB later)
users = {}  # {chat_id: {"role":"User", "balance":100}}
products = {"Free Fire Diamond": 10, "RGG Code": 5}

# ------------------ Commands ------------------

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    users.setdefault(chat_id, {"role": "User", "balance": 0})
    bot.send_message(chat_id, "💎 Welcome! Use /products to see available products.")

@bot.message_handler(commands=['products'])
def products_list(message):
    chat_id = message.chat.id
    msg = "💎 Product List & Prices:\n"
    for p, price in products.items():
        msg += f"{p} - ${price}\n"
    bot.send_message(chat_id, msg)

@bot.message_handler(commands=['wallet'])
def wallet(message):
    chat_id = message.chat.id
    balance = users.get(chat_id, {}).get("balance", 0)
    bot.send_message(chat_id, f"💎 Your balance: {balance} LKR")

@bot.message_handler(commands=['add'])
def add_balance(message):
    chat_id = message.chat.id
    user = users.get(chat_id)
    if not user or user.get("role") != "Admin":
        bot.send_message(chat_id, "❌ Only Admin can add balance.")
        return
    try:
        amount = int(message.text.split()[1])
        # for simplicity add to self (real case add to target user)
        user["balance"] += amount
        bot.send_message(chat_id, f"💎 Added {amount} LKR. New balance: {user['balance']}")
    except:
        bot.send_message(chat_id, "❌ Usage: /add <amount>")

# ------------------ Run Bot ------------------
if __name__ == "__main__":
    print("Bot running...")
    bot.infinity_polling()
