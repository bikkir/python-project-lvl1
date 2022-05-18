#!/usr/bin/env python
import random

TASK = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 30


def get_round():
    num1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    num2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    sign = random.choice('+-*')
    text_question = f'{num1} {sign} {num2}'
    correct_answer = str(eval(f'{num1}{sign}{num2}'))
    return text_question, correct_answer
