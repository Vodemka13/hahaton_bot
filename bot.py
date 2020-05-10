import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import choice
from menu_keyboard import menu_keyboard
from minigames_keyboard import minigames_keyboard
from rsp import rsp_keyboard, get_winner, yes_no_keyboard
from cities import cities, cities_keyboard, bot_turn_cities, human_turn_cities
from study import study_keyboard, mailing_keyboard
from wiki import wikip
from animals import animals
from tic_tac_toe import tic_tac_toe_keyboard, human_turn_tic_tac_toe, bot_turn_tic_tac_toe
from mailing_keyboard import mailing_it_keyboard, mailing_eng_keyboard, it_dict, eng_dict

token = '60b8ae3a1dab3b179bb60e9af23ab0af56421f9d2fb44ca8bb9e6e9da9f8ead1b5b174ed48c51284e15a4'
vk_session = vk_api.VkApi(token=token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

begin_text = 'Привет, Тебя приветствует Карантин-Бот. Надеемся, что эта маленькая и неумелая разработка поможет тебе ' \
             'скрасить твои карантиновые будни ;з \n Вот список команд. Если ты не туда нажал, можешь заново вызвать ' \
             'эту клавиатуру сообщением "Команды". И главное - не болейте! '

users = dict()

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_user and not event.from_me:
                if event.user_id not in list(users.keys()):
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': begin_text,
                                                        'keyboard': menu_keyboard(), 'random_id': 0})
                    users[event.user_id] = {'action': 'in_menu',
                                            'cities': cities[:],
                                            'city_letter': '',
                                            'board': [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]}
                    print(f'Бот: {begin_text}')
                else:
                    print(f'{event.user_id}: {event.text}')
                    msg = event.text
                    if msg.lower() == 'команды':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Держи, дружок :з',
                                                            'keyboard': menu_keyboard(), 'random_id': 0})
                        users[event.user_id] = {'action': 'in_menu',
                                                'cities': cities[:],
                                                'city_letter': '',
                                                'board': [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]}
                        print(f'Бот: Держи, дружок :з')

                    elif msg.lower() == 'обучение 📚':
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Поощраю, приятной учебы ;з',
                                           'keyboard': study_keyboard(), 'random_id': 0})
                        users[event.user_id]['action'] = 'choosing_studies'
                        print(f'Бот: Поощраю, приятной учебы ;з')

                    elif msg.lower() == 'мини игры 🎲':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Приятной игры ;з',
                                                            'keyboard': minigames_keyboard(), 'random_id': 0})
                        users[event.user_id]['action'] = 'choosing_games'
                        print(f'Бот: Приятной игры ;з')

                    elif msg.lower() == 'милые фотокарточки животных 💖':
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'В наше трудное '
                                                                                                 'время только '
                                                                                                 'зверятки спасут мир',
                                                            'keyboard': menu_keyboard(), 'attachment': choice(animals),
                                                            'random_id': 0})
                        print(f'Бот: В наше трудное время только котятки спасут мир')

                    elif users[event.user_id]['action'] == 'choosing_studies':
                        if msg.lower() == 'интересные рассылки 📨':
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Выбери категорию',
                                                                'keyboard': mailing_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_mailing'
                            print(f'Бот: Выбери категорию')
                        elif msg.lower() == 'поиск по википедии 𝞨':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Введи свой запрос',
                                               'random_id': 0})
                            users[event.user_id]['action'] = 'in_wiki'
                            print(f'Бот: Введи свой запрос')
                        elif msg.lower() == 'выход 🚪':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Можешь что-нибудь выбрать',
                                               'keyboard': menu_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'in_menu'
                            print(f'Бот: Можешь что-нибудь выбрать')

                    elif users[event.user_id]['action'] == 'in_wiki':
                        text = wikip(msg)
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': text,
                                           'keyboard': study_keyboard(), 'random_id': 0})
                        users[event.user_id]['action'] = 'choosing_studies'
                        print(f'Бот: {text}')

                    elif users[event.user_id]['action'] == 'choosing_mailing':
                        if msg.lower() == 'выход 🚪':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Можешь что-нибудь выбрать',
                                               'keyboard': study_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_studies'
                            print(f'Бот: Можешь что-нибудь выбрать')
                        elif msg.lower() == 'it 💻':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Тут представлены загаловки статей',
                                               'keyboard': mailing_it_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_it'
                            print(f'Бот: Тут представлены загаловки статей')
                        elif msg.lower() == 'английский язык 🇬🇧':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Тут представлены загаловки статей',
                                               'keyboard': mailing_eng_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_eng'
                            print(f'Бот: Тут представлены загаловки статей')

                    elif users[event.user_id]['action'] == 'choosing_it':
                        if msg.lower() == 'выход 🚪':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Можешь что-нибудь выбрать',
                                               'keyboard': mailing_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_mailing'
                            print(f'Бот: Можешь что-нибудь выбрать')
                        elif msg in list(it_dict.keys()):
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': it_dict[msg],
                                               'keyboard': mailing_it_keyboard(), 'random_id': 0})
                            print(f'Бот: ' + it_dict[msg])

                    elif users[event.user_id]['action'] == 'choosing_eng':
                        if msg.lower() == 'выход 🚪':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Можешь что-нибудь выбрать',
                                               'keyboard': mailing_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_mailing'
                            print(f'Бот: Можешь что-нибудь выбрать')
                        elif msg in list(eng_dict.keys()):
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': eng_dict[msg],
                                               'keyboard': mailing_eng_keyboard(), 'random_id': 0})
                            print(f'Бот: ' + eng_dict[msg])

                    elif users[event.user_id]['action'] == 'choosing_games':
                        if msg.lower() == 'выход 🚪':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Можешь что-нибудь выбрать',
                                               'keyboard': menu_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'in_menu'
                            print(f'Бот: Можешь что-нибудь выбрать')
                        elif msg.lower() == 'камень ножницы бумага 🎮':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Выбери свой ход',
                                               'keyboard': rsp_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_rsp'
                            print(f'Бот: Выбери свой ход')
                        elif msg.lower() == 'игра в города 🌆':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Пожалуй, я начну', 'random_id': 0})
                            users[event.user_id]['action'] = 'playing_cities'
                            print(len(cities))
                            city, users[event.user_id]['cities'], last = bot_turn_cities(cities[:],
                                                                                         users[event.user_id][
                                                                                             'city_letter'])
                            users[event.user_id]['city_letter'] = last
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': city,
                                               'keyboard': cities_keyboard(), 'random_id': 0})
                            print(f'Бот: Пожалуй, я начну' + city)
                        elif msg.lower() == 'крестики-нолики ❌⭕':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Твой ход, удачки)',
                                               'keyboard': tic_tac_toe_keyboard(users[event.user_id]['board']),
                                               'random_id': 0})
                            users[event.user_id]['action'] = 'playing_tic_tac_toe'
                            print('Бот: Твой ход, удачки)')

                    elif users[event.user_id]['action'] == 'playing_tic_tac_toe':
                        if msg.lower() == 'выход 🚪':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Ну ладно, можешь '
                                                                                    'сыграть во что-то '
                                                                                    'другое',
                                               'keyboard': minigames_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_games'
                            users[event.user_id]['board'] = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
                            users[event.user_id]['city_letter'] = ''
                            print(f'Бот: Ну ладно, можешь сыграть во что-то другое')
                        else:
                            res, users[event.user_id]['board'] = human_turn_tic_tac_toe(users[event.user_id]['board'],
                                                                                        msg)
                            if res == 'OK':
                                bot_res, text, users[event.user_id]['board'] = bot_turn_tic_tac_toe(
                                    users[event.user_id]['board'])
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id,
                                                   'message': text,
                                                   'keyboard': tic_tac_toe_keyboard(users[event.user_id]['board']),
                                                   'random_id': 0})
                                print('Бот: ' + text)
                                if bot_res == 'Again':
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id,
                                                       'message': 'Клетка занята, попробуй еще раз',
                                                       'keyboard': tic_tac_toe_keyboard(users[event.user_id]['board']),
                                                       'random_id': 0})
                                    print('Бот: Клетка занята, попробуй еще раз')
                                elif bot_res == 'Draw':
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id,
                                                       'message': 'Ничья! Хорошая игра, дружище!',
                                                       'keyboard': minigames_keyboard(), 'random_id': 0})
                                    users[event.user_id]['action'] = 'choosing_games'
                                    users[event.user_id]['board'] = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
                                    print('Бот: Ничья! Хорошая игра, дружище!')
                                elif bot_res == '❌':
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id,
                                                       'message': 'Вы победили! Спасибо за игру ;)',
                                                       'keyboard': minigames_keyboard(), 'random_id': 0})
                                    users[event.user_id]['action'] = 'choosing_games'
                                    users[event.user_id]['board'] = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
                                    print('Бот: Вы победили! Спасибо за игру ;)')
                                elif bot_res == '⭕':
                                    vk_session.method('messages.send',
                                                      {'user_id': event.user_id,
                                                       'message': 'Увы, я победил. Хорошая игра!',
                                                       'keyboard': minigames_keyboard(), 'random_id': 0})
                                    users[event.user_id]['action'] = 'choosing_games'
                                    users[event.user_id]['board'] = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
                                    print('Бот: Увы, я победил. Хорошая игра!')
                            elif res == 'Again':
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id,
                                                   'message': 'Клетка занята, попробуй еще раз',
                                                   'keyboard': tic_tac_toe_keyboard(users[event.user_id]['board']),
                                                   'random_id': 0})
                                print('Бот: Клетка занята, попробуй еще раз')
                            elif res == 'Draw':
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id, 'message': 'Ничья! Хорошая игра, дружище!',
                                                   'keyboard': minigames_keyboard(), 'random_id': 0})
                                users[event.user_id]['action'] = 'choosing_games'
                                users[event.user_id]['board'] = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
                                print('Бот: Ничья! Хорошая игра, дружище!')
                            elif res == '❌':
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id,
                                                   'message': 'Вы победили! Спасибо за игру ;)',
                                                   'keyboard': minigames_keyboard(), 'random_id': 0})
                                users[event.user_id]['action'] = 'choosing_games'
                                users[event.user_id]['board'] = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
                                print('Бот: Вы победили! Спасибо за игру ;)')
                            elif res == '⭕':
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id, 'message': 'Увы, я победил. Хорошая игра!',
                                                   'keyboard': minigames_keyboard(), 'random_id': 0})
                                users[event.user_id]['action'] = 'choosing_games'
                                users[event.user_id]['board'] = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]
                                print('Бот: Увы, я победил. Хорошая игра!')

                    elif users[event.user_id]['action'] == 'playing_cities':
                        if msg.lower() == 'выход 🚪':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Ну ладно, можешь '
                                                                                    'сыграть во что-то '
                                                                                    'другое',
                                               'keyboard': minigames_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_games'
                            users[event.user_id]['cities'] = cities[:]
                            users[event.user_id]['city_letter'] = ''
                            print(f'Бот: Ну ладно, можешь сыграть во что-то другое')
                        else:
                            res, users[event.user_id]['cities'], users[event.user_id][
                                'city_letter'] = human_turn_cities(
                                msg.capitalize(), users[event.user_id]['cities'], users[event.user_id]['city_letter'])
                            if res:
                                city, users[event.user_id]['cities'], last = bot_turn_cities(
                                    users[event.user_id]['cities'],
                                    users[event.user_id][
                                        'city_letter'])
                                users[event.user_id]['city_letter'] = last
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id, 'message': city,
                                                   'keyboard': cities_keyboard(), 'random_id': 0})
                                print(city)
                            else:
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id, 'message': 'Город либо уже был, либо ты '
                                                                                        'ошибся, попробуй еще раз ;)',
                                                   'keyboard': cities_keyboard(), 'random_id': 0})
                                print(f'Бот: Город либо уже был, либо ты ошибся, попробуй еще раз ;)')
                    elif users[event.user_id]['action'] == 'choosing_rsp':
                        results = get_winner(msg)
                        if results == 'Error':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id,
                                               'message': 'Не знаю о чем ты, попробуй еще раз',
                                               'keyboard': rsp_keyboard(), 'random_id': 0})
                            print(f'Бот: Не знаю о чем ты, попробуй еще раз')
                        else:
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': results[1], 'random_id': 0})
                            print(f'Бот: {results[1]}')
                            if results[0] == 'Draw':
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id,
                                                   'message': 'Ничья! Еще разок?',
                                                   'keyboard': yes_no_keyboard(), 'random_id': 0})
                                users[event.user_id]['action'] = 'choosing_rsp_final'
                                print(f'Бот: Ничья! Еще разок?')
                            elif results[0]:
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id,
                                                   'message': 'Увы, я победил. Еще разок?',
                                                   'keyboard': yes_no_keyboard(), 'random_id': 0})
                                users[event.user_id]['action'] = 'choosing_rsp_final'
                                print(f'Бот: Увы, я победил. Еще разок?')
                            else:
                                vk_session.method('messages.send',
                                                  {'user_id': event.user_id,
                                                   'message': 'В этот раз твоя взяла! Еще разок?',
                                                   'keyboard': yes_no_keyboard(), 'random_id': 0})
                                users[event.user_id]['action'] = 'choosing_rsp_final'
                                print(f'Бот: В этот раз ваша взяла! Еще разок?')
                    elif users[event.user_id]['action'] == 'choosing_rsp_final':
                        if msg.lower() == 'да':
                            vk_session.method('messages.send',
                                              {'user_id': event.user_id, 'message': 'Круто)\nВыбери свой ход',
                                               'keyboard': rsp_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_rsp'
                            print(f'Бот: Круто) Выбери свой ход')
                        elif msg.lower() == 'нет':
                            vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Ну ладно, можешь '
                                                                                                     'сыграть во '
                                                                                                     'что-то '
                                                                                                     'другое',
                                                                'keyboard': minigames_keyboard(), 'random_id': 0})
                            users[event.user_id]['action'] = 'choosing_games'
                            print(f'Бот: Ну ладно, можешь сыграть во что-то другое')

                    else:
                        vk_session.method('messages.send', {'user_id': event.user_id,
                                                            'message': 'Я тебя не очень понимаю :с\nНапиши "Команды", '
                                                                       'чтобы получить клавиатуру команд',
                                                            'random_id': 0})
                        print(f'Бот: Я тебя не очень понимаю :с Напиши "Команды", чтобы получить клавиатуру команд')
