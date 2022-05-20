#!/usr/bin/env python
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 4
UPPER_BOUND = 40


def get_round():
    num1 = randint(LOWER_BOUND, UPPER_BOUND)
    num2 = randint(LOWER_BOUND, UPPER_BOUND)
    text_question = f'{num1} {num2}'
    correct_answer = get_answer(num1, num2)
    return text_question, correct_answer


def get_answer(num1, num2):
    while num2 != 0:
        if num1 > num2:
            num1, num2 = num2, num1
        num2 = num2 % num1
    return str(num1)
