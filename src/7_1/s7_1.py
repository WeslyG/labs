#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ph_dict = [{
#     'name': 'Яблочный сок',
#     'value': 3.0
# }, {
#     'name': 'Шампунь',
#     'value': 5.5
# }, {
#     'name': 'Мыло для рук',
#     'range': {
#         'min': 9.0,
#         'max': 10.0
#     }
# }]


# def ph_validator(maybe_ph: str) -> float:
#     try:
#         return float(maybe_ph)
#     except Exception:
#         print('Ошибка: PH должен быть числом!')
#         exit(1)


# def user_input():
#     user_input: float = input('Введите значение PH: ')
#     return ph_getter(user_input)


# def ph_getter(value: float) -> str:
#     result: str = ''
#     for item in ph_dict:
#         if item['value']:
#             if (value == item['value']):
#                 result = item['name']
#         if item['range']:
#             if (value > item['range']['min'] and value < item['range']['max']):
#                 result = item['name']
#     else:
#         result = 'Не найдено'
#     return result
