#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN = 1
MAX = 100


def generate_question():
    number = randint(MIN, MAX)
    text_question = number
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return text_question, correct_answer


def is_even(number):
    return number % 2 == 0
