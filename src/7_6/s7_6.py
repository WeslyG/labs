#!/usr/bin/python3
# -*- coding: utf-8 -*-


def classification_of_wind(wind: int) -> str:
    if wind > 1 and wind < 4:
        return 'Слабый'
    elif wind > 5 and wind < 10:
        return 'Умеренный'
    elif wind > 9 and wind < 18:
        return 'Сильный'
    elif wind > 19:
        return 'Ураганный'
    else:
        return 'Ветер должен быть больше нуля!'
