import json
from pathlib import Path


DB_PATH = Path("data/news.json")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    if not DB_PATH.exists():
        DB_PATH.write_text(
            json.dumps(
                {
                    "news": []
                },
                ensure_ascii=False,
                indent=2
            ),
            encoding="utf-8"
        )


def load_db():
    init_db()

    return json.loads(
        DB_PATH.read_text(encoding="utf-8")
    )


def save_db(data):
    DB_PATH.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


def news_exists(url):
    data = load_db()

    return any(
        news["url"] == url
        for news in data["news"]
    )


def save_news(title, url, source):
    data = load_db()

    if news_exists(url):
        return

    data["news"].append(
        {
            "title": title,
            "url": url,
            "source": source,
            "status": "new"
        }
    )

    save_db(data)


def get_new_news(limit=10):
    data = load_db()

    news = [
        item
        for item in data["news"]
        if item["status"] == "new"
    ]

    return [
        (
            index,
            item["title"],
            item["url"],
            item["source"]
        )
        for index, item in enumerate(data["news"])
        if item["status"] == "new"
    ][:limit]


def mark_as_sent(news_id):
    data = load_db()

    if 0 <= news_id < len(data["news"]):
        data["news"][news_id]["status"] = "sent"

    save_db(data)
