#!/usr/bin/env python
from random import randint

TASK = 'What number is missing in the progression?'


def generate_question():
    num1 = randint(1, 20)
    step = randint(1, 5)
    key = randint(2, 9)
    text_question = f'{num1}'
    i = 1
    while i < 10:
        if i == key:
            text_question += ' ..'
            correct_answer = str(num1 + i * step)
        else:
            text_question += ' ' + str(num1 + i * step)
        i += 1
    return text_question, correct_answer
