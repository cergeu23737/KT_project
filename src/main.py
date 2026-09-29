import feedparser
from sources import SOURCES


def get_news():
    for source in SOURCES:
        feed = feedparser.parse(source["url"])

        print(f"\nИсточник: {source['name']}")

        for item in feed.entries[:5]:
            print(f"- {item.title}")
            print(item.link)


if __name__ == "__main__":
    get_news()
