# todo реализовать симуляцию игры камень ножницы бумага
import datetime
import random
from collections import Counter

from django.http import HttpResponse
from django.template import loader

"""
1 - Rock / Камень
2 - Scissors / Ножницы
3 - Paper / Бумага
"""

games = list()


def play_game():
    player_one = random.randint(1, 3)
    player_two = random.randint(1, 3)

    if player_one == 1 and player_two == 2:
        games.append('Player_one: Rock vs Player_two: Scissors')
        return ('Player_one')

    elif player_one == 2 and player_two == 3:
        games.append('Player_one: Scissors vs Player_two: Paper')
        return ('Player_one')

    elif player_one == 3 and player_two == 1:
        games.append('Player_one: Paper vs Player_two: Rock')
        return ('Player_one')

    elif player_one == 2 and player_two == 1:
        games.append('Player_one: Scissors vs Player_two: Rock')
        return ('Player_two')

    elif player_one == 3 and player_two == 2:
        games.append('Player_one: Paper vs Player_two: Scissors')
        return ('Player_two')

    elif player_one == 1 and player_two == 3:
        games.append('Player_one: Rock vs Player_two: Paper')
        return ('Player_two')

    elif player_one == 1 and player_two == 1:
        games.append('Player_one: Rock vs Player_two: Rock Replay')
        return ('Draw')

    elif player_one == 2 and player_two == 2:
        games.append('Player_one: Scissors vs Player_two: Scissors Replay')
        return ('Draw')

    elif player_one == 3 and player_two == 3:
        games.append('Player_one: Paper vs Player_two: Paper Replay')
        return ('Draw')


def index(request):
    current_time = datetime.datetime.now()
    winner_list = list()
    games_count = 0
    while games_count < 3:
        game_result = play_game()
        if game_result == 'Draw':
            continue
        winner_list.append(game_result)
        games_count += 1
    count = Counter(winner_list)
    winner = count.most_common(1)
    context = {
        'current_time': current_time,
        'winner': winner[0][0],
        'games': games
    }
    template = loader.get_template('/home/hardtobeagod/PycharmProjects/pycon2018-django-tutorial/mysite/templates/mysite.html')
    return HttpResponse(template.render(context, request))



# Правила камень бьет ножницы, ножницы бьют бумагу, бумага бьет камень.
# В иигре присутствуют 2 игрока:
# игрок в длинном плаще
# игрок в шляпе

# задача сгенерировать и вывести в шаблон dict cо следующим содержимым.
# {
#     'current_time': текущее время,
#     'winner': Кто победил в серии трех игр,
#     'games': Список строк, каждая из которых содержит информацию о ходе,
#           какой игрок, как ходил.
# }

# шаблон для view лежит тут
# mysite/templates/mysite.html
