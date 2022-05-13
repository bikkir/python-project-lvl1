#!/usr/bin/env python
from random import randint

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    number = randint(1, 100)
    if number == 2:
        correct_answer = 'yes'
    elif number == 1:
        correct_answer = 'no'
    i = number - 1
    while i > 1:
        if number % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
        i -= 1
    return number, correct_answer
