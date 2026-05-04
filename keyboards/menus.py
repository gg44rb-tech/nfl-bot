from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📚 База знаний", callback_data="menu_knowledge")],
        [InlineKeyboardButton(text="🇺🇸 NFL — Лига и команды", callback_data="menu_nfl")],
        [InlineKeyboardButton(text="🇷🇺 Российский футбол", callback_data="menu_russia")],
        [InlineKeyboardButton(text="🎓 Новичкам", callback_data="menu_beginners")],
        [InlineKeyboardButton(text="📊 Аналитика и прогнозы", callback_data="menu_analytics")],
        [InlineKeyboardButton(text="💎 Подписка", callback_data="menu_subscription")],
    ])


def knowledge_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📖 Терминология", callback_data="knowledge_terms")],
        [InlineKeyboardButton(text="📏 Правила игры", callback_data="knowledge_rules")],
        [InlineKeyboardButton(text="🏃 Позиции игроков", callback_data="knowledge_positions")],
        [InlineKeyboardButton(text="🏆 История спорта", callback_data="knowledge_history")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")],
    ])


def nfl_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏟️ Все 32 команды NFL", callback_data="nfl_teams")],
        [InlineKeyboardButton(text="📅 Сезон 2024/2025", callback_data="nfl_schedule")],
        [InlineKeyboardButton(text="📈 Статистика игроков", callback_data="nfl_stats")],
        [InlineKeyboardButton(text="🎯 Драфт", callback_data="nfl_draft")],
        [InlineKeyboardButton(text="🏆 История Супербоула", callback_data="nfl_superbowl")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")],
    ])


def russia_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏟️ Все команды России", callback_data="russia_teams")],
        [InlineKeyboardButton(text="🏆 Лиги и дивизионы", callback_data="russia_leagues")],
        [InlineKeyboardButton(text="📅 Календарь сезона", callback_data="russia_calendar")],
        [InlineKeyboardButton(text="📞 Контакты и соцсети", callback_data="russia_contacts")],
        [InlineKeyboardButton(text="🔍 Найти команду рядом", callback_data="russia_find")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")],
    ])


def beginners_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 С чего начать", callback_data="beginners_start")],
        [InlineKeyboardButton(text="🛡️ Экипировка", callback_data="beginners_gear")],
        [InlineKeyboardButton(text="🏃 Как попасть в команду", callback_data="beginners_join")],
        [InlineKeyboardButton(text="💪 Тренировочные программы", callback_data="beginners_training")],
        [InlineKeyboardButton(text="❓ FAQ", callback_data="beginners_faq")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")],
    ])


def subscription_kb(is_subscribed: bool = False) -> InlineKeyboardMarkup:
    if is_subscribed:
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="ℹ️ Информация о подписке", callback_data="sub_info")],
            [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")],
        ])
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⭐ Оплатить Telegram Stars", callback_data="sub_stars")],
        [InlineKeyboardButton(text="💳 Оплатить картой", callback_data="sub_pay")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_main")],
    ])


def back_kb(callback: str = "back_main") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data=callback)],
    ])
