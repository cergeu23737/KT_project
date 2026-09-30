from database import init_db, get_new_news, mark_as_sent
from telegram import send_message
from translator import translate_batch_to_russian


def send_news_queue():
    init_db()

    news_list = get_new_news(limit=10)

    if not news_list:
        print("Очередь пуста.")
        return

    titles = [
        item[1]
        for item in news_list
    ]

    translated_titles = translate_batch_to_russian(titles)

    messages = [
        "📰 НОВОСТИ",
        ""
    ]

    for number, (item, translated_title) in enumerate(
        zip(news_list, translated_titles),
        start=1
    ):
        news_id, title, url, source = item

        messages.append(
            f"{number}. {translated_title}\n"
            f"Источник: {source}"
        )

        messages.append("")

    message = "\n".join(messages).strip()

    send_message(message)

    for item in news_list:
        news_id = item[0]
        mark_as_sent(news_id)

    print(f"ОТПРАВЛЕНО ОДНИМ СООБЩЕНИЕМ: {len(news_list)} новостей")


if __name__ == "__main__":
    send_news_queue()
