import os
import asyncio

from telethon import TelegramClient

from database import init_db, news_exists, save_news


API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

CHANNEL = "tn24ch"

SESSION_NAME = "kt_news_engine"


async def collect_telegram_news():
    client = TelegramClient(
        SESSION_NAME,
        API_ID,
        API_HASH,
    )

    await client.start()

    messages = await client.get_messages(
        CHANNEL,
        limit=10,
    )

    init_db()

    for message in reversed(messages):
        if not message.text:
            continue

        title = message.text.strip()

        url = f"https://t.me/{CHANNEL}/{message.id}"

        if news_exists(url):
            print(f"УЖЕ ЕСТЬ: {title[:80]}")
            continue

        save_news(
            title=title,
            url=url,
            source="ТН",
        )

        print(f"ДОБАВЛЕНО ИЗ ТН: {title[:80]}")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(collect_telegram_news())
