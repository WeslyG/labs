#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math


def int_validator(maybe_int: str):
    try:
        return int(maybe_int)
    except Exception:
        print('Ошибка: Пожалуйста введите число!')
        exit(1)


def square_of_triangle() -> None:
    a = int_validator(input('Введите сторону a: '))
    b = int_validator(input('Введите сторону b: '))
    c = int_validator(input('Введите сторону c: '))
    p = (a + b + c) / 2
    square = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь = {square}'.format(square=square))
