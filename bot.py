import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from database.db import init_db
from handlers import start, menu, knowledge, nfl, russia, beginners, subscription, admin
from middlewares.subscription import SubscriptionMiddleware

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def main():
    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Инициализация базы данных
    await init_db()

    # Регистрация middleware
    dp.message.middleware(SubscriptionMiddleware())
    dp.callback_query.middleware(SubscriptionMiddleware())

    # Регистрация роутеров
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(knowledge.router)
    dp.include_router(nfl.router)
    dp.include_router(russia.router)
    dp.include_router(beginners.router)
    dp.include_router(subscription.router)
    dp.include_router(admin.router)

    logger.info("🏈 NFL Bot запущен!")

    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())