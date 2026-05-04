from aiogram import Router, F
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, Message
from aiogram.filters import Command

from keyboards.menus import subscription_kb, back_kb
from database.db import is_subscribed, get_subscription_info, add_subscription
from config import SUBSCRIPTION_PRICE

router = Router()


async def _subscription_text(user_id: int) -> tuple[str, bool]:
    """Возвращает (текст, is_subscribed)"""
    subscribed = await is_subscribed(user_id)
    if subscribed:
        expires = await get_subscription_info(user_id)
        text = (
            f"💎 <b>Твоя подписка активна!</b>\n\n"
            f"✅ Действует до: <b>{expires.strftime('%d.%m.%Y')}</b>\n\n"
            f"У тебя есть доступ ко всем разделам бота:\n"
            f"• 🇷🇺 Все команды России + контакты\n"
            f"• 🇺🇸 NFL полная база\n"
            f"• 🎓 Гайды для новичков\n"
            f"• 📊 Аналитика и прогнозы"
        )
    else:
        text = (
            "💎 <b>Подписка NFL Russia Bot</b>\n\n"
            f"<b>{SUBSCRIPTION_PRICE}₽ в месяц</b> — доступ ко всем материалам:\n\n"
            "✅ Все команды России с контактами менеджеров\n"
            "✅ Полная база NFL (32 команды, статистика)\n"
            "✅ Гайды для новичков (экипировка, тренировки)\n"
            "✅ Как найти команду в твоём городе\n"
            "✅ Аналитика и прогнозы матчей\n"
            "✅ Регулярные обновления контента\n\n"
            "💡 <i>Это дешевле чашки кофе, а пользы на сезон!</i>"
        )
    return text, subscribed


@router.callback_query(F.data == "menu_subscription")
async def subscription_menu(callback: CallbackQuery):
    text, subscribed = await _subscription_text(callback.from_user.id)
    await callback.message.edit_text(text, reply_markup=subscription_kb(subscribed))
    await callback.answer()


@router.callback_query(F.data == "sub_info")
async def sub_info(callback: CallbackQuery):
    text, subscribed = await _subscription_text(callback.from_user.id)
    await callback.message.edit_text(text, reply_markup=subscription_kb(subscribed))
    await callback.answer()


@router.callback_query(F.data == "sub_stars")
async def pay_stars(callback: CallbackQuery):
    """Оплата через Telegram Stars"""
    await callback.message.answer_invoice(
        title="Подписка NFL Russia Bot",
        description="Доступ ко всем материалам на 30 дней",
        payload="subscription_30days",
        currency="XTR",  # Telegram Stars
        prices=[LabeledPrice(label="Подписка 30 дней", amount=50)],  # 50 stars ≈ 100₽
    )
    await callback.answer()


@router.callback_query(F.data == "sub_pay")
async def pay_rub(callback: CallbackQuery):
    """Оплата через ЮКасса (требует подключения провайдера)"""
    await callback.message.edit_text(
        "💳 <b>Оплата картой</b>\n\n"
        "Для оплаты картой (ЮКасса) необходимо подключить платёжный провайдер.\n\n"
        "Пока что используй оплату через Telegram Stars ⭐\n\n"
        "<i>Если возникли вопросы — используй /help</i>",
        reply_markup=back_kb("menu_subscription")
    )
    await callback.answer()


@router.pre_checkout_query()
async def pre_checkout(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


@router.message(F.successful_payment)
async def successful_payment(message: Message):
    """Успешная оплата — активируем подписку"""
    await add_subscription(message.from_user.id)
    await message.answer(
        "🎉 <b>Подписка активирована!</b>\n\n"
        "Теперь тебе доступны все разделы бота на 30 дней.\n\n"
        "Используй /start чтобы вернуться в главное меню. 🏈"
    )


@router.message(Command("sub"))
async def cmd_sub(message: Message):
    subscribed = await is_subscribed(message.from_user.id)
    if subscribed:
        expires = await get_subscription_info(message.from_user.id)
        await message.answer(
            f"✅ Подписка активна до {expires.strftime('%d.%m.%Y')}",
            reply_markup=subscription_kb(True)
        )
    else:
        await message.answer(
            "❌ Подписка не активна.",
            reply_markup=subscription_kb(False)
        )
