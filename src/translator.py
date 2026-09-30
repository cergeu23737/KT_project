import os
import requests


TRANSLATE_URL = os.getenv(
    "TRANSLATE_URL",
    "https://libretranslate.com/translate"
)

TRANSLATE_API_KEY = os.getenv("TRANSLATE_API_KEY")


def translate_to_russian(text):
    data = {
        "q": text,
        "source": "auto",
        "target": "ru",
        "format": "text",
    }

    if TRANSLATE_API_KEY:
        data["api_key"] = TRANSLATE_API_KEY

    response = requests.post(
        TRANSLATE_URL,
        json=data,
        timeout=20,
    )

    response.raise_for_status()

    result = response.json()

    return result["translatedText"]
