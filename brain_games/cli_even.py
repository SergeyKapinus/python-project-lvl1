
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
    if name == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_even(number):
    return number % 2 == 0


def get_integer():
    return random.randint(0, 10)


def get_answer():
    return prompt.string('Your answer: ')


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


def get_range():
    numbers = range(0, 50, random.randint(2, 5))
    for i in numbers:
        list_numbers = list(numbers)
    return list_numbers


def get_progression(list_numbers):
    l_copy = list_numbers.copy()
    i_random = random.randint(0, len(l_copy)-1)
    l_copy.pop(i_random)
    l_copy.insert(i_random, '..')
    return l_copy


def get_string(list_numbers):
    return ' '.join(map(str, list_numbers))


def is_prime(number):
    d = 2
    if number == 1:
        return False
    while number % 2 != 0:
        d += 1
    return d == number
