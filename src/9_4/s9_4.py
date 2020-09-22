#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import randint


def int_validator(maybe_int: str):
    try:
        return int(maybe_int)
    except Exception:
        print('Ошибка: Пожалуйста введите число!')
        exit(1)


def get_random_int(min, max) -> int:
    return randint(min, max)


def guess_number():
    comp_number: int = get_random_int(1, 10)
    user_number = int_validator(input('Угадай число от 1 до 10: '))
    while user_number != comp_number:
        user_number = int_validator(input('Повторите еще раз: '))
    print('Победа!')
