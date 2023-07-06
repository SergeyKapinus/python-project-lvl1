#!/usr/bin/env python3


from brain_games.games.cli import greet_hello, get_name, greet_hello_user, get_discription, get_answer
from brain_games.games.game_gcd import gcd
from brain_games.games.getting_integer import get_integer


def play_gcd(name):
    i = 1
    while i <= 3:
        a = get_integer()
        b = get_integer()
        print(f'Question: {a} {b}')
        answer = get_answer()
        if answer == gcd(a, b):
            print('Correct!')
        else:
            return print(f"'{str(answer)}' is wrong answer ;(. Correct answer was '{gcd(a, b)}'.\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')


def main():
    greet_hello()
    name = get_name()
    greet_hello_user(name)
    get_discription('gcd')
    play_gcd(name)


if __name__ == '__main__':
    main()
