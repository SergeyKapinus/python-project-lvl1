#!/usr/bin/env python3


from brain_games.cli_even import greet_hello, get_name, get_discription, greet_hello_user
from brain_games.cli_even import get_integer, get_answer, get_operator, calc


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
    get_discription('calc')
    play_calc(name)


if __name__ == '__main__':
    main()
