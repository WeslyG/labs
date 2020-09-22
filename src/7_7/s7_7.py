#!/usr/bin/python3
# -*- coding: utf-8 -*-

db_dict = [{
    'id': 1,
    'name': 'Красный зал',
    'film_name': 'Пятница',
    'sessions': [{
        'time': 12,
        'price': 250
    }, {
        'time': 16,
        'price': 350
    }, {
        'time': 20,
        'price': 450
    }]
}, {
    'id': 2,
    'name': 'Синий зал',
    'film_name': 'Чемпионы: Быстрее. Выше. Сильнее',
    'sessions': [{
        'time': 10,
        'price': 250
    }, {
        'time': 13,
        'price': 350
    }, {
        'time': 16,
        'price': 350
    }]
}, {
    'id': 3,
    'name': 'Голубой зал',
    'film_name': 'Пернатая банда',
    'sessions': [{
        'time': 10,
        'price': 350
    }, {
        'time': 14,
        'price': 450
    }, {
        'time': 18,
        'price': 450
    }]
}]


def persent_formula(price: int, percent: int) -> float:
    return (price * percent) / 100


def sale_calculator(tiket_price: int, tiket_count: int) -> float:
    basic_price: int = tiket_count * tiket_price
    if (tiket_count > 10):
        return basic_price - persent_formula(basic_price, 10)
    elif (tiket_count > 5):
        return basic_price - persent_formula(basic_price, 5)
    else:
        return basic_price


def ticket_calculator(room_id: int, session_time: int, tiket_count: int) -> float:
    price: int = 0
    for room in db_dict:
        if room['id'] == room_id:
            for session in room['sessions']:
                if session['time'] == session_time:
                    price = sale_calculator(session['price'], tiket_count)
    return price
