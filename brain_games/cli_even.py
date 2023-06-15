import random
import prompt


def greet_hello():
    print('Welcome to the Brain Games!')


def get_name():
    return prompt.string('May I have your name? ')


def get_discription():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def get_integer():
    return random.randint(0, 100)


def get_answer():
    return prompt.string('Yuor answer: ')


def play_even():
    greet_hello()
    name = get_name()
    print(f'Hello, {name}!')
    get_discription()
    i = 1
    while i <= 3:
        number = get_integer()
        print(f'Question: {number}')
        answer = get_answer()
        if is_even(number) and answer == 'yes' or not is_even(number) and answer == 'no':
            print('Correct!')
        elif is_even(number) and answer == 'no':
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        i += 1
    return print(f'Congratulations, {name}!')
