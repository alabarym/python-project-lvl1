# -*- coding:utf-8 -*-

"""Function declaration to verify the answers."""

import prompt
import random


def check_if_even(number):
    """Return true if even."""
    if number % 2 == 0:
        return True
    return False


def even_game():
    """
    Verify the correct answer.

    Test what does the user type in: yes or not.
    Other characters are not allowed.
    Verify the correct answer provided by user.

    Returns:
        True ot False according to the provided answer by user.
    """
    random_number = random.randint(0, 100)
    even_result = check_if_even(random_number)
    print(random_number)
    answer = prompt.string("Answer 'yes' if number even otherwise answer 'no'.\n")
    while answer == 'yes':
        if even_result:
            return True
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        return False
    while answer == 'no':
        if not even_result:
            return True
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        return False


def even_game_logic(name):
    """Even game main logic."""
    counter = 1
    while counter <= 3:
        received_value = even_game()
        if received_value:
            print('Correct!')
            if counter == 3:
                print('Congratulations, ', name, '!', sep='')
        else:
            print("Let's try again,")
            break
        counter += 1
