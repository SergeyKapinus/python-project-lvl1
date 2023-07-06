#!/usr/bin/env python3


from brain_games.games.cli import greet_hello, get_name, greet_hello_user, get_discription, get_answer
from brain_games.games.game_even import is_even
from brain_games.games.getting_integer import get_integer


def play_even(name):
    i = 1
    while i <= 3:
        number = get_integer()
        print(f'Question: {number}')
        answer = get_answer()
        if is_even(number) and answer == 'yes' or not is_even(number) and answer == 'no':
            print('Correct!')
        if is_even(number) and answer != 'yes':
            return print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
        if not is_even(number) and answer != 'no':
            return print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')


def main():
    greet_hello()
    name = get_name()
    greet_hello_user(name)
    get_discription('even')
    play_even(name)


if __name__ == '__main__':
    main()
