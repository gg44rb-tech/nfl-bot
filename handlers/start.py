from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.menus import main_menu_kb

router = Router()

WELCOME_TEXT = """
🏈 <b>Добро пожаловать в NFL Russia Bot!</b>

Самый полный русскоязычный справочник по американскому футболу — <b>полностью бесплатно!</b>

📚 <b>Что есть в боте:</b>
• Терминология, правила, позиции игроков
• Все 32 команды NFL + статистика
• Команды России и как найти свою
• Гайды для новичков — экипировка, тренировки
• История Супербоула и драфта

Выбери раздел 👇
"""

HELP_TEXT = """
ℹ️ <b>Помощь по боту</b>

<b>Команды:</b>
/start — главное меню
/help — эта справка
/sub — статус подписки

<b>Разделы:</b>
📚 <b>База знаний</b> — правила, термины, позиции
🇺🇸 <b>NFL</b> — команды, статистика, Супербоул
🇷🇺 <b>Россия</b> — команды, лиги, расписание
🎓 <b>Новичкам</b> — как начать, экипировка
💎 <b>Подписка</b> — расширенный доступ

<b>Вопросы и предложения:</b>
Напиши администратору — все обращения читаются!
"""


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb())


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(HELP_TEXT, reply_markup=main_menu_kb())
