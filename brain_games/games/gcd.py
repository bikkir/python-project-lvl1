#!/usr/bin/env python
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
MIN = 4
MAX = 40


def generate_question():
    num1 = randint(MIN, MAX)
    num2 = randint(MIN, MAX)
    text_question = f'{num1} {num2}'
    correct_answer = get_answer(num1, num2)
    return text_question, correct_answer


def get_answer(num1, num2):
    divisor = min(num1, num2)
    while not (num1 % divisor == 0 and num2 % divisor == 0):
        divisor -= 1
    return str(divisor)
