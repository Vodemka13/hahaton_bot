import json

it_dict = {
    'Финсектор во время пандемии': 'https://netology.ru/blog/finance-pandemia?utm_source=newsletter'
                                                     '&utm_medium=email&utm_campaign=brand_all_newsletter_2020_05_07',
    'Автомобильные бренды во время пандемии': 'https://netology.ru/blog/04-2020-issledovanie-auto-pandemia'
                                                      '?utm_source=newsletter&utm_medium=email&utm_campaign'
                                                      '=brand_all_newsletter_2020_05_07',
    'Что ожидать от подкастов': 'https://netology.ru/blog/05-2020-podkast-obsudili-media?utm_source=newsletter'
                                '&utm_medium=email&utm_campaign=brand_all_newsletter_2020_05_07',
    'Сммщики SkyEng': 'https://netology.ru/blog/04-2020-kak-obuchat-smm-skyeng?utm_source=newsletter&utm_medium=email'
                      '&utm_campaign=brand_all_newsletter_2020_05_07',
    'Дайджест по DataScience': 'https://netology.ru/blog/04-2020-data-science-digest?utm_source'
                                                 '=newsletter&utm_medium=email&utm_campaign=brand_all_newsletter_2020_05_07',
    'Давайте после майских': 'http://email.netology.ru/view.html?x=a62e&m=JLa&mc=t&s=zZWRa&u=z&z=fUy7oyL&',
    'Будущая статья 1': '', 'Будущая статья 2': '', 'Будущая статья 3': '', 'Будущая статья 4': '', 'Будущая '
                                                                                                    'статья '
                                                                                                    '5': '',
    'Будущая статья 6': '', 'Будущая статья 7': '', 'Будущая статья 8': '', 'Будущая статья 9': '',
    'Будущая статья 10': '', }
eng_dict = {'Hello or hi?': 'http://email.content.skyeng.ru/deliveries/RIuzBAEAAXHg9xJ9NWLWUkURmlzONA==', 'Английский '
                                                                                                          'про '
                                                                                                          'Coding':
    'http://email.content.skyeng.ru/deliveries/RIuzBAEAAXHg9rx5oacKKCEAAzFxrA==',
            'Letter of proposal': 'http://email.content.skyeng.ru/deliveries/RIuzBAEAAXHg9rx5oacKKCEAAzFxrA==',
            'Cover letter': 'http://email.content.skyeng.ru/deliveries/RIuzBAEAAXHo_-ItjWE9Wt6eucQ5hA==',
            'C:\\Vocabulary\\Documentation': 'http://email.content.skyeng.ru/deliveries'
                                             '/RIuzBAEAAXHqgEzG6XLgpFCJ1Bgm_w==',
            'Icebreakers': 'http://email.content.skyeng.ru/deliveries/RIuzBAEAAXHv3lUHaxxfxeh-movLkw==',
            'Будущая статья 1': '',
            'Будущая статья 2': '', 'Будущая статья 3': '', 'Будущая статья 4': '', 'Будущая статья 5': '',
            'Будущая статья 6': '', 'Будущая статья 7': '', 'Будущая статья 8': '', 'Будущая статья 9': '',
            'Будущая статья 10': '', }


def mailing_it_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": list(it_dict.keys())[0]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": list(it_dict.keys())[1]
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": list(it_dict.keys())[2]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": list(it_dict.keys())[3]
                },
                "color": "secondary"
            }, ], [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": list(it_dict.keys())[4]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": list(it_dict.keys())[5]
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": list(it_dict.keys())[6]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": list(it_dict.keys())[7]
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"5\"}",
                    "label": list(it_dict.keys())[8]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"5\"}",
                    "label": list(it_dict.keys())[9]
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


def mailing_eng_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": list(eng_dict.keys())[0]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": list(eng_dict.keys())[1]
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": list(eng_dict.keys())[2]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": list(eng_dict.keys())[3]
                },
                "color": "secondary"
            }, ], [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": list(eng_dict.keys())[4]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": list(eng_dict.keys())[5]
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": list(eng_dict.keys())[6]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"4\"}",
                    "label": list(eng_dict.keys())[7]
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"5\"}",
                    "label": list(eng_dict.keys())[8]
                },
                "color": "secondary"
            }, {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"5\"}",
                    "label": list(eng_dict.keys())[9]
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
