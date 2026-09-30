from database import init_db, get_new_news, mark_as_sent
from telegram import send_message
from translator import translate_to_russian


def send_news_queue():
    init_db()

    news_list = get_new_news(limit=10)

    if not news_list:
        print("Очередь пуста.")
        return

    for news_id, title, url, source in news_list:
        translated_title = translate_to_russian(title)

        message = (
            f"📰 {translated_title}\n\n"
            f"Источник: {source}"
        )

        send_message(message)
        mark_as_sent(news_id)

        print(f"ОТПРАВЛЕНО: {translated_title}")


if __name__ == "__main__":
    send_news_queue()
