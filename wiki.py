import wikipediaapi


wik = wikipediaapi.Wikipedia('ru', extract_format=wikipediaapi.ExtractFormat.WIKI)


def wikip(msg):
    if wik.page(msg).exists():
        return f"Неполный текст статьи: {wik.page(msg).text[:200]}... \n Тут можно найти полный текст статьи: {wik.page(msg).fullurl}"
    return 'К сожалению, такой страницы нет на Вики :с\nПроверь, не ошибся ли ты (даже регистр важен)'


