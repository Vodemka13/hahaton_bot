import json
from random import choice


def rsp_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "&#128511;"
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "&#9996;"
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "&#128196;"
                },
                "color": "secondary"
            }, ]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard


def get_winner(msg):
    reply = choice(['🗿', '✌', '📄'])
    if msg == '🗿':
        if reply == '📄':
            return [True, reply]
        elif reply == '✌':
            return [False, reply]
        elif reply == '🗿':
            return ['Draw', reply]
    elif msg == '✌':
        if reply == '🗿':
            return [True, reply]
        elif reply == '📄':
            return [False, reply]
        elif reply == '✌':
            return ['Draw', reply]
    elif msg == '📄':
        if reply == '✌':
            return [True, reply]
        elif reply == '🗿':
            return [False, reply]
        elif reply == '📄':
            return ['Draw', reply]
    else:
        return 'Error'


def yes_no_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Да"
                },
                "color": "positive"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Нет"
                },
                "color": "negative"
            }]
        ]
    }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard
