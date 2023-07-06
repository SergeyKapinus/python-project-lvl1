import prompt


def greet_hello():
    print('Welcome to the Brain Games!')


def get_name():
    return prompt.string('May I have your name? ')


def greet_hello_user(name):
    print(f'Hello, {name}!')


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


def get_answer():
    return prompt.string('Your answer: ')
