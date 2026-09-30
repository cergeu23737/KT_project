import feedparser

from sources import SOURCES
from database import init_db, news_exists, save_news
from version import check_version


def collect_news():
    init_db()

    for source in SOURCES:
        print(f"\n=== {source['name']} ===")

        try:
            feed = feedparser.parse(source["url"])

            if not feed.entries:
                print("НЕТ НОВОСТЕЙ ИЛИ RSS НЕДОСТУПЕН")
                continue

            for item in feed.entries[:5]:
                title = getattr(item, "title", "").strip()
                url = getattr(item, "link", "").strip()

                if not title or not url:
                    continue

                if news_exists(url):
                    print(f"УЖЕ ЕСТЬ: {title}")
                    continue

                save_news(title, url, source["name"])

                print(f"ДОБАВЛЕНО В ОЧЕРЕДЬ: {title}")

        except Exception as error:
            print(f"ОШИБКА ИСТОЧНИКА: {error}")


if __name__ == "__main__":
    check_version()
    collect_news()
