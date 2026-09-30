import os

from telethon import TelegramClient


API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")

CHANNEL = "tn24ch"

client = TelegramClient(
    "kt_news_engine",
    API_ID,
    API_HASH,
)


async def get_channel_news():
    await client.start()

    messages = await client.get_messages(
        CHANNEL,
        limit=10,
    )

    news = []

    for message in messages:
        if not message.text:
            continue

        news.append({
            "title": message.text,
            "source": "ТН",
            "telegram_id": message.id,
        })

    return news


if __name__ == "__main__":
    import asyncio

    news = asyncio.run(get_channel_news())

    for item in news:
        print(item)
