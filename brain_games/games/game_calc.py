import random


DISCRIPTION = 'What is the result of the expression?'


def get_operator():
    return random.choice(['+', '-', '*'])


def calc(a, operator, b):
    if operator == '+':
        return str(a + b)
    if operator == '-':
        return str(a - b)
    if operator == '*':
        return str(a * b)
