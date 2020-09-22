#!/usr/bin/python3
# -*- coding: utf-8 -*-

from s7_7 import ticket_calculator


def test_s7_7():
    assert ticket_calculator(3, 10, 5) == 1750
    assert ticket_calculator(3, 10, 6) == 1995
    assert ticket_calculator(1, 16, 11) == 3465
    # Не найден зал
    assert ticket_calculator(5, 0, 10) == 0
    # Билетов 0
    assert ticket_calculator(1, 16, 0) == 0
