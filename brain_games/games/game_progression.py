import random


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