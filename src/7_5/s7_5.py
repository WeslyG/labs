#!/usr/bin/python3
# -*- coding: utf-8 -*-

user_dict = [{
    'sity': 'Екатеринбург',
    'code': 343,
    'price': 15
}, {
    'sity': 'Омск',
    'code': 381,
    'price': 18
}, {
    'sity': 'Воронеж',
    'code': 473,
    'price': 13
}, {
    'sity': 'Ярославль',
    'code': 485,
    'price': 11
}]


def calculate_price(sity_code: int, duration: int) -> int:
    result: int = 0
    for i in user_dict:
        if i['code'] == sity_code:
            result = i['price'] * duration
    return result
