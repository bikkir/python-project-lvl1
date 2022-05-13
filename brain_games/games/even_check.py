#!/usr/bin/env python
from random import randint

task = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    number = randint(1, 100)
    text_question = number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return text_question, correct_answer
