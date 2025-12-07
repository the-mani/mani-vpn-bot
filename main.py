```python
import os
import json
import time
from typing import Optional
from telebot import TeleBot, types

# ---------------- CONFIG (اینها را تغییر نده — BOT_TOKEN را در Render به عنوان env var ست کن)
ADMIN_ID = 8014203768  # آیدی عددی ادمین (مانی)
CARD_NUMBER = "6219861907741234"  # شماره کارتت را اینجا بذار اگر می‌خوای در متن نمایش داده شود
STORAGE_FILE = "storage.json"

# ---------------- Bot init
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable not set")

bot = TeleBot(TOKEN, parse_mode=None)
