#!/usr/bin/env python3


from brain_games.cli_even import greet_hello, get_name, get_discription
from brain_games.cli_even import is_prime, get_integer, get_answer


def play_prime():
    greet_hello()
    name = get_name()
    print(f'Hello, {name}!')
    get_discription('prime')
    i = 1
    while i <= 3:
        number = get_integer()
        print(f'Question: {number}')
        answer = get_answer()
        if is_prime(number) and answer == 'yes' or not is_prime(number) and answer == 'no':
            print('Correct!')
        elif is_prime(number) and answer == 'no':
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')


def main():
    play_prime()


if __name__ == '__main__':
    main()
