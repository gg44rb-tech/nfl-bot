import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# Администраторы (Telegram user_id через запятую)
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "123456789").split(",")))

# Подписка
SUBSCRIPTION_PRICE = 100  # рублей
SUBSCRIPTION_DAYS = 30

# Платёжный провайдер (ЮКасса)
YOOKASSA_SHOP_ID = os.getenv("YOOKASSA_SHOP_ID", "")
YOOKASSA_SECRET_KEY = os.getenv("YOOKASSA_SECRET_KEY", "")

# База данных
DATABASE_PATH = "nfl_bot.db"
