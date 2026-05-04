from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.menus import main_menu_kb, knowledge_kb, nfl_kb, russia_kb, beginners_kb, back_kb

router = Router()


@router.callback_query(F.data == "back_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "🏈 <b>Главное меню</b>\n\nВыбери раздел:",
        reply_markup=main_menu_kb()
    )
    await callback.answer()


@router.callback_query(F.data == "menu_knowledge")
async def menu_knowledge(callback: CallbackQuery):
    await callback.message.edit_text(
        "📚 <b>База знаний</b>\n\n"
        "Здесь собрана вся базовая информация об американском футболе.\n"
        "Этот раздел доступен <b>бесплатно</b>! 🎉",
        reply_markup=knowledge_kb()
    )
    await callback.answer()


@router.callback_query(F.data == "menu_nfl")
async def menu_nfl(callback: CallbackQuery):
    await callback.message.edit_text(
        "🇺🇸 <b>NFL — Национальная футбольная лига</b>\n\n"
        "Всё о профессиональном американском футболе: команды, игроки, статистика.",
        reply_markup=nfl_kb()
    )
    await callback.answer()


@router.callback_query(F.data == "menu_russia")
async def menu_russia(callback: CallbackQuery):
    await callback.message.edit_text(
        "🇷🇺 <b>Российский американский футбол</b>\n\n"
        "Всё о командах России: контакты, расписание, как вступить.",
        reply_markup=russia_kb()
    )
    await callback.answer()


@router.callback_query(F.data == "menu_beginners")
async def menu_beginners(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎓 <b>Новичкам</b>\n\n"
        "Только пришёл в спорт? Здесь всё что нужно знать для старта.",
        reply_markup=beginners_kb()
    )
    await callback.answer()


@router.callback_query(F.data == "menu_analytics")
async def menu_analytics(callback: CallbackQuery):
    await callback.message.edit_text(
        "📊 <b>Аналитика и прогнозы</b>\n\n"
        "🚧 Раздел в разработке. Скоро здесь появятся разборы матчей и прогнозы!",
        reply_markup=back_kb("back_main")
    )
    await callback.answer()
