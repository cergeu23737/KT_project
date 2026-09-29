import feedparser

from sources import SOURCES
from database import init_db, news_exists, save_news


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

            save_news(title, url)

            print(f"НОВАЯ НОВОСТЬ: {title}")
            print(f"Ссылка: {url}")


if __name__ == "__main__":
    get_news()
