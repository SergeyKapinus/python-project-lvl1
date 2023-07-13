#!/usr/bin/env python3


from brain_games.games.cli import greet_hello, get_name, greet_hello_user, get_discription, get_answer
from brain_games.games.game_progression import get_range, get_progression, get_string, DISCRIPTION


def play_progression(name):
    i = 1
    while i <= 3:
        range = get_range()
        progression = get_progression(range)
        str_progression = get_string(progression)
        print(f'Question: {str_progression}')
        answer = get_answer()
        index = progression.index('..')
        if answer == str(range[index]):
            print('Correct!')
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{range[index]}'.\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')


def main():
    greet_hello()
    name = get_name()
    greet_hello_user(name)
    get_discription(DISCRIPTION)
    play_progression(name)


if __name__ == '__main__':
    main()
