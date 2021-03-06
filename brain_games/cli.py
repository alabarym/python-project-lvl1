# -*- coding:utf-8 -*-
"""Greeing to the users by name."""

import prompt


def greet_first():
    """First greeting message."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """
    Ask users name and store it.

    Returns:
        name of the user.
    """
    user_name = prompt.string('May I know your name? ')
    print('Hello, ', user_name, '!', sep='')
    return user_name
