#!/usr/bin/env python
from random import randint, choice

TASK = 'What number is missing in the progression?'
LOWER_BOUND = 1
INITIAL_UPPER_BOUND = 20
DIFF_UPPER_BOUND = 5


def get_round():
    progression = get_progression()
    key = choice(progression)
    text_question = ' '.join([
        '..' if num == key else str(num) for num in progression
    ])
    return text_question, str(key)


def get_progression():
    initial = randint(LOWER_BOUND, INITIAL_UPPER_BOUND)
    diff = randint(LOWER_BOUND, DIFF_UPPER_BOUND)
    max_num = initial + (diff * 10)
    return range(initial, max_num, diff)
