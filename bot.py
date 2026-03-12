import telebot
import json
import requests

# -----------------------------
# Telegram Bot Setup
# -----------------------------
BOT_TOKEN = "8799375203:AAEbldBCM66UiShErsHzHxRO9nejgot7kO0"  # BotFather token
bot = telebot.TeleBot(BOT_TOKEN)

# -----------------------------
# Database (JSON in-memory, replace with real DB)
# -----------------------------
users = {}  # chat_id : {role: "User"/"Admin", balance: int}
products = {"Free Fire Diamond": 10, "RGG Code": 5}
transactions = []  # store topup / rgg / payment verification

WEB_CHAT_ID = "8324590734"  # For auto notify web orders

# -----------------------------
# Helper function: Send web order to Telegram
# -----------------------------
def send_web_order(customer_name, product, qty):
    message = f"🛒 New Order Received!\nCustomer: {customer_name}\nProduct: {product}\nQty: {qty}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": WEB_CHAT_ID, "text": message}
    requests.post(url, data=payload)

# -----------------------------
# User Commands
# -----------------------------
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    users.setdefault(chat_id, {"role": "User", "balance": 0})
    bot.send_message(chat_id, "💎 Welcome to Kaviya Auto Topup Bot!\nUse /products to see available items.")

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

# Example: /id <uid> <product> <qty>
@bot.message_handler(commands=['id'])
def topup_id(message):
    chat_id = message.chat.id
    try:
        parts = message.text.split()
        uid = parts[1]
        product = parts[2]
        qty = int(parts[3])
        # Store transaction
        transactions.append({"user": chat_id, "uid": uid, "product": product, "qty": qty})
        bot.send_message(chat_id, f"✅ Topup request received for {product} x{qty}")
        # Notify admin / web chat
        send_web_order(f"User {chat_id}", product, qty)
    except:
        bot.send_message(chat_id, "❌ Usage: /id <uid> <product> <qty>")

# -----------------------------
# Admin Commands
# -----------------------------
def is_admin(chat_id):
    return users.get(chat_id, {}).get("role") == "Admin"

@bot.message_handler(commands=['add'])
def add_balance(message):
    chat_id = message.chat.id
    if not is_admin(chat_id):
        bot.send_message(chat_id, "❌ Only Admin can use this command.")
        return
    try:
        amount = int(message.text.split()[1])
        # For simplicity, add to self (can be extended to add to other users)
        users[chat_id]["balance"] += amount
        bot.send_message(chat_id, f"💎 Added {amount} LKR. New balance: {users[chat_id]['balance']}")
    except:
        bot.send_message(chat_id, "❌ Usage: /add <amount>")

# -----------------------------
# Run Bot
# -----------------------------
if __name__ == "__main__":
    print("💎 Kaviya Auto Topup Bot is running...")
    bot.infinity_polling()
