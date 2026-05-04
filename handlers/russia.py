from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.menus import russia_kb, back_kb

router = Router()


@router.callback_query(F.data == "russia_teams")
async def russia_teams(callback: CallbackQuery):
    text = """
🇷🇺 <b>Команды России по американскому футболу</b>

<b>Москва и МО:</b>
🏈 <b>Moscow Patriots</b> — один из старейших клубов России
🏈 <b>Moscow Spartans</b> — многократные чемпионы страны
🏈 <b>Rhinos Moscow</b> — сильный московский клуб
🏈 <b>Eastern Bears</b> — команда востока Москвы
🏈 <b>Black Storm</b> — агрессивный стиль игры

<b>Санкт-Петербург:</b>
🏈 <b>St. Petersburg Griffins</b> — флагман северной столицы
🏈 <b>Neva Bulls</b> — молодая и амбициозная команда

<b>Урал:</b>
🏈 <b>Ural Mammoths</b> (Екатеринбург) — сильнейшая команда региона
🏈 <b>Perm Bears</b> (Пермь)

<b>Сибирь:</b>
🏈 <b>Siberian Bears</b> (Новосибирск)
🏈 <b>Krasnoyarsk Yenisei</b> (Красноярск)

<b>Поволжье и Юг:</b>
🏈 <b>Kazan Tigers</b> (Казань)
🏈 <b>Samara Spartans</b> (Самара)
🏈 <b>Krasnodar Cobras</b> (Краснодар)
🏈 <b>Rostov Rhinos</b> (Ростов-на-Дону)
🏈 <b>Volgograd Steel</b> (Волгоград)

<i>Раздел пополняется — скоро будут контакты каждой команды!</i>
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_russia"))
    await callback.answer()


@router.callback_query(F.data == "russia_leagues")
async def russia_leagues(callback: CallbackQuery):
    text = """
🏆 <b>Лиги и дивизионы России</b>

<b>РАФФ</b> — Российская Ассоциация Американского Футбола
Главная организация, управляющая спортом в стране с 2000-х годов.

<b>Национальная Суперлига (НСЛ)</b>
Высший дивизион страны. Борьба за главный трофей — Кубок Варягов. Участвуют сильнейшие команды со всей России.

<b>Высшая лига</b>
Второй по силе дивизион. Победитель получает путёвку в НСЛ.

<b>Первая лига</b>
Региональные дивизионы: Центр, Север-Запад, Урал, Сибирь, Юг.

<b>Дивизион развития</b>
Для новых команд — отличный старт для только созданных клубов.

<b>Студенческая лига</b>
Соревнования между университетскими командами по всей стране.

<b>Флаг-футбол</b>
Бесконтактная версия игры. Очень популярна среди новичков, женщин и детей. Не нужна дорогая экипировка!

<b>Пляжный футбол</b>
Летние турниры на песке — набирает популярность в южных городах.
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_russia"))
    await callback.answer()


@router.callback_query(F.data == "russia_contacts")
async def russia_contacts(callback: CallbackQuery):
    text = """
📞 <b>Контакты и соцсети</b>

<b>РАФФ (официальный сайт):</b>
🌐 raff.ru
📱 VK: vk.com/raff_ru

<b>Ключевые команды:</b>

🏈 <b>Moscow Patriots</b>
📱 VK: vk.com/moscowpatriots
📧 Написать тренеру через VK

🏈 <b>Moscow Spartans</b>
📱 VK: vk.com/mosspartans

🏈 <b>St. Petersburg Griffins</b>
📱 VK: vk.com/griffins_spb

🏈 <b>Ural Mammoths</b>
📱 VK: vk.com/uralmammoths

🏈 <b>Kazan Tigers</b>
📱 VK: vk.com/kazantigers

<b>💡 Совет:</b>
Большинство команд активны ВКонтакте — ищи по названию команды + город. Пиши в личку — тренеры всегда отвечают новичкам!

<i>Раздел пополняется — скоро будут прямые контакты менеджеров!</i>
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_russia"))
    await callback.answer()


@router.callback_query(F.data == "russia_calendar")
async def russia_calendar(callback: CallbackQuery):
    text = """
📅 <b>Календарь сезона 2025</b>

<b>Весенний сезон (основной):</b>
🏈 Апрель — старт регулярного сезона
🏈 Май-Июнь — туры регулярного сезона
🏈 Июль — плей-офф
🏈 Август — финал, Кубок Варягов

<b>Осенний сезон:</b>
🏈 Сентябрь — старт
🏈 Октябрь-Ноябрь — регулярный сезон
🏈 Ноябрь — плей-офф и финал

<b>Флаг-футбол:</b>
Турниры проходят круглый год, особенно активно летом.

<b>Где следить за расписанием:</b>
🌐 raff.ru — официальное расписание
📱 VK группы команд — анонсы игр
📺 Некоторые матчи транслируются онлайн

<i>Следи за обновлениями в боте — будем добавлять конкретные даты!</i>
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_russia"))
    await callback.answer()


@router.callback_query(F.data == "russia_find")
async def russia_find(callback: CallbackQuery):
    text = """
🔍 <b>Найти команду в своём городе</b>

<b>Способ 1 — через РАФФ:</b>
Зайди на raff.ru → раздел "Команды" → выбери свой регион

<b>Способ 2 — ВКонтакте:</b>
Поищи "[твой город] американский футбол" в поиске групп

<b>Способ 3 — Telegram:</b>
Поищи "[твой город] AmFootball" или "[твой город] NFL"

<b>Крупные города — где точно есть команды:</b>
🏈 Москва — 10+ команд
🏈 Санкт-Петербург — 5+ команд
🏈 Екатеринбург, Казань, Краснодар
🏈 Новосибирск, Самара, Ростов-на-Дону
🏈 Пермь, Красноярск, Волгоград
🏈 Уфа, Нижний Новгород, Воронеж

<b>Нет команды в городе?</b>
Можно создать свою! РАФФ помогает новым командам с регистрацией. Нужно минимум 20-25 человек для старта.

<b>Напиши свой город</b> в чат — помогу найти конкретную команду! 🏈
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_russia"))
