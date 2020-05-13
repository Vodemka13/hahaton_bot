import json


def minigames_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Камень ножницы бумага &#127918;"
                },
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Игра в города &#127750;"
                },
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": "Крестики-Нолики ❌⭕"
                },
                "color": "primary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Милые фотокарточки животных &#128150;"
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
