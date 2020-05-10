import json
from random import randint


def tic_tac_toe_keyboard(board):
    keyboard = {
        "one_time": False,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": board[0][0] + ' (1, 1)'
                },
                "color": "secondary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": board[0][1] + ' (1, 2)'
                },
                "color": "secondary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": board[0][2] + ' (1, 3)'
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": board[1][0] + ' (2, 1)'
                },
                "color": "secondary"
            },
                {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": board[1][1] + ' (2, 2)'
                },
                "color": "secondary"
            },
                {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": board[1][2] + ' (2, 3)'
                },
                "color": "secondary"
            }, ],
            [{
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": board[2][0] + ' (3, 1)'
                },
                "color": "secondary"
            },
                {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": board[2][1] + ' (3, 2)'
                },
                "color": "secondary"
            },
                {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"3\"}",
                    "label": board[2][2] + ' (3, 3)'
                },
                "color": "secondary"
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


def check_cell(board, x, y):
    if board[x][y] == '#':
        return True
    return False


def check_win(board):
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != '#':
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != '#':
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != '#':
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != '#':
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != '#':
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != '#':
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != '#':
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != '#':
        return board[0][2]
    else:
        return False


def is_map_full(board):
    for row in board:
        if '#' in row:
            return False
    return True


def human_turn_tic_tac_toe(board, msg):
    msg = msg.split(',')
    x, y = int(msg[0][-1]) - 1, int(msg[1][1]) - 1
    if check_cell(board, x, y):
        board[x][y] = '❌'
        if not check_win(board):
            if not is_map_full(board):
                return ['OK', board]
            return ['Draw', board]
        return [check_win(board), board]
    return ['Again', board]


def bot_turn_tic_tac_toe(board):
    turn_done = False
    x, y = None, None
    while not turn_done:
        x, y = randint(0, 2), randint(0, 2)
        if check_cell(board, x, y):
            board[x][y] = '⭕'
            turn_done = True
    if not check_win(board):
        if not is_map_full(board):
            return ['OK', f'Я сходил на ({x}, {y})', board]
        return ['Draw', f'Я сходил на ({x}, {y})', board]
    return [check_win(board), f'Я сходил на ({x}, {y})', board]
