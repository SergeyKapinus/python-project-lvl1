#!/usr/bin/env python3
import random
import prompt


<<<<<<< HEAD
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

=======
def greet_hello():
    print('Welcome to the Brain Games!')


def get_name():
    return prompt.string('May I have your name? ')


def get_discription(name):
    if name == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    if name == 'calc':
        print('What is the result of the expression?')
    if name == 'gcd':
        print('Find the greatest common divisor of given numbers.')
    if name == 'progression':
        print('What number is missing in the progression?')


def get_integer():
    return random.randint(0, 10)

def get_answer():
    return prompt.string('Your answer: ')

def get_range():
    numbers = range(0, 50, random.randint(2, 5))
    for i in numbers:
        l = list(numbers)
    return l

def get_progression(l):
    i_random = random.randint(0, len(l)-1)
    l.pop(i_random)
    l.insert(i_random, '..')
    return l

# def play_progression():
#     greet_hello()
#     name = get_name()
#     print(f'Hello, {name}!')
#     get_discription('progression')
#     i = 1
#     while i <= 3:

def get_string(l):
    return ' '.join(map(str, l))

print(get_range())
print(get_progression(get_range()))
string = get_string(get_progression(get_range()))
print(string)






















# def main():
#     play_progression()


# if __name__ == '__main__':
#     main()
>>>>>>> 4a01c2899bd054fda8ca843256e3fdd24d575108
