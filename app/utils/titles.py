def get_page_title(page_type=None):
    base_title = "Веб платформа для мастеров ручного творчества"

    titles = {
        'home': base_title,
        'shop': f"Магазин | {base_title}",
        'profile': f"Профиль | {base_title}",
        'about': f"О нас | {base_title}",
        'account': f"Мой аккаунт | {base_title}",
        'default': base_title
    }

    return titles.get(page_type, titles['default'])