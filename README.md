# 🏈 NFL Russia Bot

Полный телеграм-бот об американском футболе для русскоязычной аудитории.

## 📁 Структура проекта

```
nfl_bot/
├── bot.py                  # Точка входа
├── config.py               # Конфигурация
├── requirements.txt        # Зависимости
├── .env.example            # Шаблон переменных окружения
├── handlers/
│   ├── start.py            # /start команда
│   ├── menu.py             # Главное меню и навигация
│   ├── knowledge.py        # База знаний (БЕСПЛАТНО)
│   ├── nfl.py              # NFL раздел (платно)
│   ├── russia.py           # Российский футбол (платно)
│   ├── beginners.py        # Новичкам (платно)
│   ├── subscription.py     # Управление подпиской
│   └── admin.py            # Панель администратора
├── keyboards/
│   └── menus.py            # Все кнопки и клавиатуры
├── database/
│   └── db.py               # SQLite база данных
└── middlewares/
    └── subscription.py     # Регистрация пользователей
```

## 🚀 Установка и запуск

### 1. Создай бота в Telegram
1. Открой @BotFather в Telegram
2. Напиши `/newbot`
3. Придумай имя и юзернейм
4. Скопируй токен

### 2. Узнай свой Telegram ID
Напиши боту @userinfobot — он покажет твой user_id

### 3. Настрой сервер (VPS — Timeweb/Beget)
```bash
# Обновляем систему
sudo apt update && sudo apt upgrade -y

# Устанавливаем Python
sudo apt install python3.11 python3.11-venv python3-pip -y

# Клонируем проект
mkdir nfl_bot && cd nfl_bot
# Загрузи файлы через sftp или git
```

### 4. Установи зависимости
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Настрой переменные
```bash
cp .env.example .env
nano .env
# Заполни BOT_TOKEN и ADMIN_IDS
```

### 6. Запусти бота
```bash
python bot.py
```

### 7. Автозапуск через systemd
```bash
sudo nano /etc/systemd/system/nflbot.service
```

Содержимое файла:
```ini
[Unit]
Description=NFL Russia Telegram Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/nfl_bot
ExecStart=/root/nfl_bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable nflbot
sudo systemctl start nflbot
sudo systemctl status nflbot
```

## 💎 Система подписки

### Telegram Stars (встроено, работает сразу)
Пользователи платят через встроенную систему Telegram Stars.
- Настрой количество Stars в `handlers/subscription.py` (параметр `amount`)

### ЮКасса (карты РФ)
1. Зарегистрируйся на yookassa.ru
2. Получи Shop ID и Secret Key
3. Заполни в `.env`
4. Настрой webhook

## 🔧 Команды администратора

| Команда | Описание |
|---------|----------|
| `/admin` | Панель с общей статистикой |
| `/stats` | Быстрая статистика |
| `/give_sub [user_id]` | Выдать подписку пользователю |

## 📊 Дорожная карта

- [x] Структура бота и навигация
- [x] База знаний (терминология, правила, позиции)
- [x] Система подписки (Telegram Stars)
- [x] Панель администратора
- [ ] Наполнение контентом по командам России
- [ ] Контакты менеджеров всех команд
- [ ] Интеграция с NFL API (реальная статистика)
- [ ] Поиск команды по городу
- [ ] Аналитика и прогнозы
- [ ] Рассылки и уведомления
- [ ] Оплата картой (ЮКасса)

## 📞 Поддержка

Если возникли вопросы по настройке — обращайся к разработчику.
