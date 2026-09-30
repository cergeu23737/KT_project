import feedparser

from sources import SOURCES
from database import init_db, news_exists, save_news
from telegram import send_message


def get_news():
    init_db()

    for source in SOURCES:
        print(f"\n=== {source['name']} ===")

        feed = feedparser.parse(source["url"])

        for item in feed.entries[:5]:
            title = item.title
            url = item.link

            if news_exists(url):
                print(f"УЖЕ ЕСТЬ: {title}")
                continue

            message = (
                f"📰 {title}\n\n"
                f"Источник: {source['name']}\n"
                f"🔗 {url}"
            )

            send_message(message)
            save_news(title, url)

            print(f"ОТПРАВЛЕНО: {title}")


if __name__ == "__main__":
    get_news()
