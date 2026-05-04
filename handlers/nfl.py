from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.menus import nfl_kb, back_kb

router = Router()


@router.callback_query(F.data == "nfl_teams")
async def nfl_teams(callback: CallbackQuery):
    text = """
🏟️ <b>32 команды NFL</b>

<b>NFC North:</b>
🐻 Chicago Bears | 🧀 Green Bay Packers
🦁 Detroit Lions | 🐺 Minnesota Vikings

<b>NFC South:</b>
🐈 Carolina Panthers | 🦅 Atlanta Falcons
⚜️ New Orleans Saints | 🏴‍☠️ Tampa Bay Buccaneers

<b>NFC East:</b>
🌟 Dallas Cowboys | 🦅 Philadelphia Eagles
🗽 NY Giants | 🎖️ Washington Commanders

<b>NFC West:</b>
🐏 LA Rams | 🌊 Seattle Seahawks
🦅 Arizona Cardinals | 🏔️ San Francisco 49ers

<b>AFC North:</b>
🐦 Baltimore Ravens | 🐻 Cleveland Browns
⚡ Pittsburgh Steelers | 🐅 Cincinnati Bengals

<b>AFC South:</b>
🐃 Houston Texans | 🐴 Indianapolis Colts
🐆 Jacksonville Jaguars | 🎸 Tennessee Titans

<b>AFC East:</b>
🏈 New England Patriots | 🐬 Miami Dolphins
🦬 Buffalo Bills | ✈️ NY Jets

<b>AFC West:</b>
⚡ Las Vegas Raiders | 🔱 LA Chargers
🐴 Denver Broncos | 🏹 Kansas City Chiefs
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_nfl"))
    await callback.answer()


@router.callback_query(F.data == "nfl_schedule")
async def nfl_schedule(callback: CallbackQuery):
    text = """
📅 <b>Сезон NFL 2024/2025</b>

<b>Регулярный сезон:</b>
Сентябрь 2024 — январь 2025
18 недель, 17 игр у каждой команды

<b>Плей-офф:</b>
🏆 Дивизионные раунды — январь 2025
🏆 Чемпионаты конференций — январь 2025
🏆 Супербоул LIX — февраль 2025

<b>Супербоул LIX:</b>
📍 Caesars Superdome, Новый Орлеан
📅 9 февраля 2025
🏆 Philadelphia Eagles 40:22 Kansas City Chiefs
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_nfl"))
    await callback.answer()


@router.callback_query(F.data == "nfl_stats")
async def nfl_stats(callback: CallbackQuery):
    text = """
📈 <b>Лучшие игроки сезона 2024/2025</b>

<b>🏈 Квотербеки (пасы):</b>
1. Джален Хёртс (PHI) — 4151 ярд, 29 ТД
2. Патрик Махоумс (KC) — 4183 ярд, 26 ТД
3. Ламар Джексон (BAL) — 4172 ярд, 41 ТД

<b>🏃 Раннингбеки (бег):</b>
1. Дерик Генри (BAL) — 1921 ярд, 16 ТД
2. Сакуон Баркли (PHI) — 2005 ярд, 13 ТД
3. Джош Джейкобс (GB) — 1329 ярд, 9 ТД

<b>🎯 Ресиверы (приём):</b>
1. Джа'Марр Чейз (CIN) — 1708 ярд, 17 ТД
2. Джастин Джефферсон (MIN) — 1533 ярд, 10 ТД
3. Купер Капп (SF) — 1380 ярд, 8 ТД

<b>🛡️ Защита (сэки):</b>
1. Ти Джей Уотт (PIT) — 11.5 сэков
2. Михаил Мэтт (MIN) — 10 сэков
3. Брайан Бёрнс (NYG) — 9 сэков
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_nfl"))
    await callback.answer()


@router.callback_query(F.data == "nfl_draft")
async def nfl_draft(callback: CallbackQuery):
    text = """
🎯 <b>NFL Драфт — как это работает</b>

<b>Что такое драфт?</b>
Ежегодное событие где команды NFL выбирают лучших студенческих игроков. Проводится каждую весну (апрель).

<b>Структура:</b>
• 7 раундов
• 32 команды делают по 1 пику в каждом раунде
• Итого ~257 игроков за драфт

<b>Порядок выборов:</b>
Команды с худшими результатами выбирают первыми — это помогает выравнивать силы в лиге.

<b>Драфт 2024 — топ пики:</b>
1️⃣ Калеб Уильямс (QB) → Chicago Bears
2️⃣ Джейден Дэниэлс (QB) → Washington Commanders
3️⃣ Дрейк Мэй (QB) → New England Patriots
4️⃣ Марвин Харрисон Jr. (WR) → Arizona Cardinals
5️⃣ Олтиман Митчелл (WR) → LA Chargers

<b>Комбайн:</b>
Перед драфтом игроки проходят физические тесты — бег на 40 ярдов, прыжки, жим лёжа. Результаты влияют на место в драфте.
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_nfl"))
    await callback.answer()


@router.callback_query(F.data == "nfl_superbowl")
async def nfl_superbowl(callback: CallbackQuery):
    text = """
🏆 <b>История Супербоула</b>

<b>Последние 10 лет:</b>
• 2025 (LIX) — Philadelphia Eagles 40:22 Kansas City Chiefs
• 2024 (LVIII) — Kansas City Chiefs 25:22 San Francisco 49ers
• 2023 (LVII) — Kansas City Chiefs 38:35 Philadelphia Eagles
• 2022 (LVI) — LA Rams 23:20 Cincinnati Bengals
• 2021 (LV) — Tampa Bay Buccaneers 31:9 Kansas City Chiefs
• 2020 (LIV) — Kansas City Chiefs 31:20 San Francisco 49ers
• 2019 (LIII) — New England Patriots 13:3 LA Rams
• 2018 (LII) — Philadelphia Eagles 41:33 New England Patriots
• 2017 (LI) — New England Patriots 34:28 Atlanta Falcons (OT)
• 2016 (50) — Denver Broncos 24:10 Carolina Panthers

<b>Самые титулованные:</b>
🏆 New England Patriots — 6 побед
🏆 Pittsburgh Steelers — 6 побед
🏆 San Francisco 49ers — 5 побед
🏆 Dallas Cowboys — 5 побед
🏆 Kansas City Chiefs — 4 победы
"""
    await callback.message.edit_text(text, reply_markup=back_kb("menu_nfl"))
