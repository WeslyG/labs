#!/usr/bin/python3
# -*- coding: utf-8 -*-

def int_validator(maybe_int: str):
    try:
        return int(maybe_int)
    except Exception:
        print('Ошибка: Пожалуйста введите число!')
        exit(1)


def user_input() -> list:
    one = input('Введите первое число: ')
    two = input('Введите второе число: ')
    tree = input('Введите третье число: ')
    return [int_validator(one), int_validator(two), int_validator(tree)]


def summ_of_tree_numbers(one: float, two: float, tree: float) -> float:
    return one + two + tree


def multipy_of_tree_numbers(one: float, two: float, tree: float) -> float:
    return one * two * tree


def main() -> None:
    user_array: list = user_input()
    summ: float = summ_of_tree_numbers(one=user_array[0], two=user_array[1], tree=user_array[2])
    multiply: float = multipy_of_tree_numbers(one=user_array[0], two=user_array[1], tree=user_array[2])
    print('Сумма введеных чисел: {summ}'.format(summ=summ))
    print('Произведение введеных чисел: {multiply}'.format(multiply=multiply))
