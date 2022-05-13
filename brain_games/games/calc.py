#!/usr/bin/env python
import random

task = 'What is the result of the expression?'


def generate_question():
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    sign = random.choice('+-*')
    if sign == '*':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

    text_question = (f'{num1} {sign} {num2}')
    correct_answer = str(eval(f'{num1}{sign}{num2}'))
    return text_question, correct_answer
