import aiosqlite
from datetime import datetime, timedelta
from config import DATABASE_PATH, SUBSCRIPTION_DAYS


async def init_db():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id     INTEGER PRIMARY KEY,
                username    TEXT,
                full_name   TEXT,
                joined_at   TEXT DEFAULT (datetime('now')),
                is_banned   INTEGER DEFAULT 0
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                user_id     INTEGER PRIMARY KEY,
                expires_at  TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS payments (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id     INTEGER,
                amount      INTEGER,
                payment_id  TEXT,
                status      TEXT DEFAULT 'pending',
                created_at  TEXT DEFAULT (datetime('now'))
            )
        """)
        await db.commit()


async def get_or_create_user(user_id: int, username: str, full_name: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            """INSERT OR IGNORE INTO users (user_id, username, full_name)
               VALUES (?, ?, ?)""",
            (user_id, username, full_name)
        )
        await db.execute(
            """UPDATE users SET username=?, full_name=? WHERE user_id=?""",
            (username, full_name, user_id)
        )
        await db.commit()


async def is_subscribed(user_id: int) -> bool:
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute(
            "SELECT expires_at FROM subscriptions WHERE user_id=?", (user_id,)
        )
        row = await cursor.fetchone()
        if not row:
            return False
        expires_at = datetime.fromisoformat(row[0])
        return expires_at > datetime.now()


async def add_subscription(user_id: int):
    expires_at = datetime.now() + timedelta(days=SUBSCRIPTION_DAYS)
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            """INSERT INTO subscriptions (user_id, expires_at)
               VALUES (?, ?)
               ON CONFLICT(user_id) DO UPDATE SET expires_at=excluded.expires_at""",
            (user_id, expires_at.isoformat())
        )
        await db.commit()


async def get_subscription_info(user_id: int):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute(
            "SELECT expires_at FROM subscriptions WHERE user_id=?", (user_id,)
        )
        row = await cursor.fetchone()
        if not row:
            return None
        return datetime.fromisoformat(row[0])


async def get_stats():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute("SELECT COUNT(*) FROM users")
        total_users = (await cursor.fetchone())[0]

        cursor = await db.execute(
            "SELECT COUNT(*) FROM subscriptions WHERE expires_at > datetime('now')"
        )
        active_subs = (await cursor.fetchone())[0]

        cursor = await db.execute(
            "SELECT COUNT(*) FROM users WHERE joined_at >= datetime('now', '-1 day')"
        )
        new_today = (await cursor.fetchone())[0]

        return {
            "total_users": total_users,
            "active_subs": active_subs,
            "new_today": new_today
        }
