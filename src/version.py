from config import VERSION, LATEST_VERSION


def check_version():
    if VERSION != LATEST_VERSION:
        print(
            f"🆕 Доступна новая версия KT News Engine: "
            f"{LATEST_VERSION}"
        )
        print(
            f"Текущая версия: {VERSION}"
        )
        print(
            "Рекомендуется перейти на новую версию."
        )
        return False

    print(f"✅ Версия KT News Engine актуальна: {VERSION}")
    return True
