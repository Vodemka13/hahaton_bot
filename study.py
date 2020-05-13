import json


def study_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Информационный раздел &#128242;"
                },
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Интересные рассылки &#128232;"
                },
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Поиск по Википедии &#120744;"
                },
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": "Выход &#128682;"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard


def mailing_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "IT &#128187;"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Английский язык 🇬🇧"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Выход &#128682;"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard


def info_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Таблица sin, cos, tg, ctg"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Таблица квадратов"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Степени мнимой единицы"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": "Таблица натуральных логарифмов"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": "Таблица десятичных логарифмов"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"5\"}",
                    "label": "Таблица логарифмов по основанию а"
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"6\"}",
                    "label": "Выход &#128682;"
                },
                "color": "negative"
            }, ]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard
