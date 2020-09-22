#!/usr/bin/python3
# -*- coding: utf-8 -*-


def ph_validator(maybe_ph: str) -> float:
    try:
        return float(maybe_ph)
    except Exception:
        print('Ошибка: PH должен быть числом!')
        exit(1)


def ph_getter() -> None:
    user_input: float = ph_validator(input('Введите значение PH(float): '))
    if user_input == 3.0:
        print('Яблочный сок')
    elif user_input == 5.5:
        print('Шампунь')
    elif user_input > 9.0 and user_input < 10.0:
        print('Мыло для рук')
    else:
        print('Не найдено')
