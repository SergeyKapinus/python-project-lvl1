#!/usr/bin/env python3


from brain_games.cli_even import greet_hello, get_name, get_discription
from brain_games.cli_even import get_answer, get_range, get_progression, get_string


def play_progression():
    greet_hello()
    name = get_name()
    print(f'Hello, {name}!')
    get_discription('progression')
    i = 1
    while i <= 3:
        range = get_range() # список последовательности
        progression = get_progression(range) # список последовательности с '..'
        str_progression = get_string(progression) # строка последовательности с '..'
        print(f'Question: {str_progression}')
        answer = get_answer()
        index = progression.index('..')
        if int(answer) == range[index]:
            print('Correct!')
        else:
            return print(f"'{str(answer)}' is wrong answer ;(. Correct answer was '{range[index]}'.\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')


def main():
    play_progression()


if __name__ == '__main__':
    main()

