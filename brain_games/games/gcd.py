#!/usr/bin/env python
from random import randint

task = 'Find the greatest common divisor of given numbers.'


def generate_question():
    num1 = randint(4, 40)
    num2 = randint(4, 40)
    divisor = min(num1, num2)
    while not (num1 % divisor == 0 and num2 % divisor == 0):
        divisor -= 1
    text_question = f'{num1} {num2}'
    correct_answer = str(divisor)
    return text_question, correct_answer
