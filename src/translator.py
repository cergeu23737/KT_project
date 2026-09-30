from deep_translator import GoogleTranslator


def translate_batch_to_russian(texts):
    if not texts:
        return []

    try:
        translator = GoogleTranslator(
            source="auto",
            target="ru"
        )

        translated = translator.translate_batch(texts)

        print("ПЕРЕВОД ВЫПОЛНЕН")

        return translated

    except Exception as error:
        print(f"ОШИБКА ПЕРЕВОДА: {error}")

        return texts
