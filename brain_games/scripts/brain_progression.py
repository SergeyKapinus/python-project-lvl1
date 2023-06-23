#!/usr/bin/env python3
import random
import prompt


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
