from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.filters import BaseFilter

from database.db import get_stats, add_subscription
from config import ADMIN_IDS

router = Router()


class IsAdmin(BaseFilter):
    async def __call__(self, event) -> bool:
        user_id = None
        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id
        return user_id in ADMIN_IDS


@router.message(Command("admin"), IsAdmin())
async def admin_panel(message: Message):
    stats = await get_stats()
    text = (
        f"⚙️ <b>Панель администратора</b>\n\n"
        f"👥 Всего пользователей: <b>{stats['total_users']}</b>\n"
        f"💎 Активных подписок: <b>{stats['active_subs']}</b>\n"
        f"🆕 Новых сегодня: <b>{stats['new_today']}</b>\n\n"
        f"<b>Команды:</b>\n"
        f"/give_sub [user_id] — выдать подписку\n"
        f"/stats — статистика\n"
        f"/broadcast — рассылка (в разработке)"
    )
    await message.answer(text)


@router.message(Command("stats"), IsAdmin())
async def admin_stats(message: Message):
    stats = await get_stats()
    await message.answer(
        f"📊 Пользователей: {stats['total_users']}\n"
        f"💎 Подписок: {stats['active_subs']}\n"
        f"🆕 Новых сегодня: {stats['new_today']}"
    )


@router.message(Command("give_sub"), IsAdmin())
async def give_sub(message: Message):
    args = message.text.split()
    if len(args) < 2:
        await message.answer("Использование: /give_sub [user_id]")
        return
    try:
        user_id = int(args[1])
        await add_subscription(user_id)
        await message.answer(f"✅ Подписка выдана пользователю {user_id}")
    except ValueError:
        await message.answer("❌ Неверный user_id")
