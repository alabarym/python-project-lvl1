# -*- coding:utf-8 -*-

"""Main cli module for even game."""

import even_check
import prompt
import random


def even_game():
    random_number = random.randint(0, 10000)
    even_result = even_check.check_if_even(random_number)
    print(random_number)
    answer = prompt.string(prompt="Answer 'yes' if number even otherwise answer 'no'.\n")
    while str(answer) != 'no' and str(answer) != 'yes':
        answer = prompt.string(
            prompt="Answer 'yes' if number even otherwise answer 'no'.\n")
    if str(answer) == 'yes' and even_result == True:
        print("Correct!")
        return True
    elif str(answer) == 'no' and even_result == False:
        print("Correct!")
        return True
    elif str(answer) == 'yes' and even_result == False:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False
    elif str(answer) == 'no' and even_result == True:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False
