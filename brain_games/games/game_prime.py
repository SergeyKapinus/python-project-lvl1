import math


DISCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    limit = math.sqrt(number)
    i = 2
    while i <= limit:
        if number % i == 0:
            return False
        i += 1
    return True
