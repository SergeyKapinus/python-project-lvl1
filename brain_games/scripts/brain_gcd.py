#!/usr/bin/env python3


from brain_games.cli_even import greet_hello, get_name, get_discription
from brain_games.cli_even import get_integer, get_answer, gcd, greet_hello_user


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
