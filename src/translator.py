from deep_translator import GoogleTranslator


def translate_to_russian(text):
    text = text.strip()

    if not text:
        return text

    try:
        translator = GoogleTranslator(
            source="auto",
            target="ru"
        )

        translated = translator.translate(text)

        print(f"ПЕРЕВОД: {text} -> {translated}")

        if translated:
            return translated

    except Exception as error:
        print(f"ОШИБКА ПЕРЕВОДА: {error}")

    return text
