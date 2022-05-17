#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN = 1
MAX = 100


def generate_question():
    number = randint(MIN, MAX)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def is_prime(number):
    if number == 2:
        return True
    elif number == 1:
        return False
    else:
        i = number
        while i > 2:
            i -= 1
            if number % i == 0:
                return False
        return True
