import telebot

BOT_TOKEN = "8799375203:AAEbldBCM66UiShErsHzHxRO9nejgot7kO0"  # BotFather token
WEB_CHAT_ID = "8324590734"  # Admin / group chat

bot = telebot.TeleBot(BOT_TOKEN)

# ----------------- Commands Help -----------------
commands_list = """
💎 Available Commands:

User:
- /start - Start bot
- /products - Product list & prices
- /wallet - Check balance
- /report - Last 2 days report
- /id <uid> <product> [qty] - Free Fire diamond top-up
- /rgg <code1> [code2…] - Redeem RGG codes (max 5)
- /verify <transaction_id> - Verify payment & add LKR

Admin:
- /add <amount> - Add balance [Admin Only]
- /deduct <amount> - Deduct balance [Admin Only]
- /signout - Remove user [Admin Only]
- /signup - Register user [Admin Only]
- /role <User|Admin> - Change role [Admin Only]
"""

users = {}  # chat_id: {"role":"User"/"Admin", "balance":int}

# ----------------- Command Handlers -----------------
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    users.setdefault(chat_id, {"role":"User", "balance":0})
    bot.send_message(chat_id, "💎 Welcome to Kaviya Auto Topup Bot!\nType /help to see commands.")

@bot.message_handler(commands=['help'])
def help_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, commands_list)

@bot.message_handler(commands=['wallet'])
def wallet(message):
    chat_id = message.chat.id
    balance = users.get(chat_id, {}).get("balance",0)
    bot.send_message(chat_id, f"💎 Your balance: {balance} LKR")

# Example /id command
@bot.message_handler(commands=['id'])
def topup_id(message):
    chat_id = message.chat.id
    try:
        parts = message.text.split()
        uid = parts[1]
        product = parts[2]
        qty = int(parts[3])
        bot.send_message(chat_id, f"✅ Topup request received for {product} x{qty}")
        bot.send_message(WEB_CHAT_ID, f"🛒 Order: User {chat_id}, {product} x{qty}")
    except:
        bot.send_message(chat_id, "❌ Usage: /id <uid> <product> <qty>")

# ----------------- Admin Check -----------------
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
        users[chat_id]["balance"] += amount
        bot.send_message(chat_id, f"💎 Added {amount} LKR. New balance: {users[chat_id]['balance']}")
    except:
        bot.send_message(chat_id, "❌ Usage: /add <amount>")

# ----------------- Run Bot -----------------
if __name__ == "__main__":
    print("💎 Kaviya Auto Topup Bot is running...")
    bot.infinity_polling()
