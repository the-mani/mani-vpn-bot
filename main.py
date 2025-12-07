import telebot
import os
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# --- Load storage.json ---
def load_configs():
    try:
        with open("storage.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("configs", [])
    except:
        return []

# --- Save storage.json ---
def save_configs(configs):
    with open("storage.json", "w", encoding="utf-8") as f:
        json.dump({"configs": configs}, f, ensure_ascii=False, indent=4)

config_list = load_configs()

# --- Commands ---

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! به ربات فروش کانفیگ خوش اومدی 🌐\n\nبرای خرید /buy رو بزن.")

@bot.message_handler(commands=['add'])
def add_config(message):
    if message.from_user.id != 8014203768:
        bot.reply_to(message, "اجازه نداری ⚠️")
        return
    
    cfg = message.text.replace("/add ", "").strip()
    if cfg:
        config_list.append(cfg)
        save_configs(config_list)
        bot.reply_to(message, "کانفیگ اضافه شد ✔️")
    else:
        bot.reply_to(message, "مثل این:\n/add vmess://xxxx")

@bot.message_handler(commands=['list'])
def list_configs(message):
    if message.from_user.id != 8014203768:
        bot.reply_to(message, "اجازه نداری ⚠️")
        return
    
    if not config_list:
        bot.reply_to(message, "لیست خالیه ❗")
    else:
        result = "\n\n".join(config_list)
        bot.reply_to(message, f"کانفیگ‌ها:\n\n{result}")

@bot.message_handler(commands=['buy'])
def buy(message):
    if not config_list:
        bot.reply_to(message, "کانفیگی موجود نیست ❗")
        return

    cfg = config_list.pop(0)
    save_configs(config_list)
    bot.reply_to(message, f"کانفیگت:\n\n{cfg}")

bot.infinity_polling()
