#!/usr/bin/python3
# -*- coding: utf-8 -*-

from s7_6 import classification_of_wind


def test_s7_6():
    assert classification_of_wind(3) == 'Слабый'
    assert classification_of_wind(9) == 'Умеренный'
    assert classification_of_wind(12) == 'Сильный'
    assert classification_of_wind(99) == 'Ураганный'
    assert classification_of_wind(0) == 'Ветер должен быть больше нуля!'
    assert classification_of_wind(-5) == 'Ветер должен быть больше нуля!'
