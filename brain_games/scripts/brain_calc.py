#!/usr/bin/env python3


from brain_games.games.cli import greet_hello, get_name, greet_hello_user, get_discription, get_answer
from brain_games.games.game_calc import get_operator, calc, DISCRIPTION
from brain_games.games.getting_integer import get_integer


def play_calc(name):
    i = 1
    while i <= 3:
        a = get_integer()
        b = get_integer()
        operator = get_operator()
        print(f'Question: {a} {operator} {b}')
        answer = get_answer()
        if answer == calc(a, operator, b):
            print('Correct!')
        else:
            return print(f"'{str(answer)}' is wrong answer ;(. Correct answer was '{calc(a, operator, b)}'.\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')


def main():
    greet_hello()
    name = get_name()
    greet_hello_user(name)
    get_discription(DISCRIPTION)
    play_calc(name)


if __name__ == '__main__':
    main()
