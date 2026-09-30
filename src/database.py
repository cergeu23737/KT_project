import sqlite3
from pathlib import Path


DB_PATH = Path("data/news.db")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                source TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'new',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        db.commit()


def news_exists(url):
    with sqlite3.connect(DB_PATH) as db:
        result = db.execute(
            "SELECT 1 FROM news WHERE url = ?",
            (url,)
        ).fetchone()

        return result is not None


def save_news(title, url, source):
    with sqlite3.connect(DB_PATH) as db:
        db.execute(
            """
            INSERT OR IGNORE INTO news
            (title, url, source)
            VALUES (?, ?, ?)
            """,
            (title, url, source)
        )

        db.commit()


def get_new_news(limit=10):
    with sqlite3.connect(DB_PATH) as db:
        return db.execute(
            """
            SELECT id, title, url, source
            FROM news
            WHERE status = 'new'
            ORDER BY id ASC
            LIMIT ?
            """,
            (limit,)
        ).fetchall()


def mark_as_sent(news_id):
    with sqlite3.connect(DB_PATH) as db:
        db.execute(
            "UPDATE news SET status = 'sent' WHERE id = ?",
            (news_id,)
        )

        db.commit()
