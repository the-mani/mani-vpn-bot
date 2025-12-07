import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# این لیست کانفیگ‌هاست که خودت دستی اضافه می‌کنی
config_list = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! به ربات فروش کانفیگ خوش اومدی 🌐\n\nبرای خرید /buy رو بزن.")

@bot.message_handler(commands=['add'])
def add_config(message):
    # فقط آی‌دی خودت اجازه اضافه کردن کانفیگ داشته باشه
    if message.from_user.id != 8014203768:
        bot.reply_to(message, "اجازه نداری ⚠️")
        return
    
    cfg = message.text.replace("/add ", "").strip()
    if cfg:
        config_list.append(cfg)
        bot.reply_to(message, "کانفیگ اضافه شد ✔️")
    else:
        bot.reply_to(message, "فرمت اشتباهه. مثل:\n/add vmess://xxxx")

@bot.message_handler(commands=['list'])
def list_configs(message):
    if message.from_user.id != 8014203768:
        bot.reply_to(message, "اجازه نداری ⚠️")
        return
    
    if not config_list:
        bot.reply_to(message, "لیست کانفیگ‌ها خالیه ❗")
    else:
        result = "\n\n".join(config_list)
        bot.reply_to(message, f"لیست کانفیگ‌ها:\n\n{result}")

@bot.message_handler(commands=['buy'])
def buy(message):
    if not config_list:
        bot.reply_to(message, "کانفیگی موجود نیست ❗")
        return

    cfg = config_list.pop(0)
    bot.reply_to(message, f"کانفیگت آماده‌ست:\n\n{cfg}")

bot.infinity_polling()
