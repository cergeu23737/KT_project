import feedparser
from sources import SOURCES


def get_news():
    for source in SOURCES:
        print(f"\n=== {source['name']} ===")

        feed = feedparser.parse(source["url"])

        for item in feed.entries[:5]:
            print(f"📰 {item.title}")
            print(f"🔗 {item.link}")
            print()


if __name__ == "__main__":
    get_news()
