import prompt


def greet_hello():
    print('Welcome to the Brain Games!')


def get_name():
    return prompt.string('May I have your name? ')


def greet_hello_user(name):
    print(f'Hello, {name}!')


def get_discription(discription):
    print(discription)


def get_answer():
    return prompt.string('Your answer: ')
