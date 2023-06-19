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


def is_even(number):
    return number % 2 == 0


def get_integer():
    return random.randint(0, 10)


def get_answer():
    return prompt.string('Yuor answer: ')


def get_operator():
    return random.choice(['+', '-', '*'])


def calc(a, operator, b):
    if operator == '+':
        return str(a + b)
    if operator == '-':
        return str(a - b)
    if operator == '*':
        return str(a * b)
    

def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return str(n)
