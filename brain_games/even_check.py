#!/usr/bin/env python
from random import randint
import prompt


sol = True
x = randint(1, 99)


def check():
    x = randint(1, 99)
    answer = prompt.string(f'Question: {x} \nYour answer is: ')
    if answer == 'yes' and x % 2 == 0 or answer == 'no' and x % 2 != 0:
        sol = True
        print('Correct!')
    elif x % 2 == 0:
        sol = False
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
    else:
        sol = False
        print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
    print(sol)
    return sol

sol = sol
