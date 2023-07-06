#!/usr/bin/env python3


from brain_games.cli_even import greet_hello, get_name, get_discription, greet_hello_user
from brain_games.cli_even import get_answer, get_range, get_progression, get_string


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
    get_discription('progression')
    play_progression(name)


if __name__ == '__main__':
    main()
