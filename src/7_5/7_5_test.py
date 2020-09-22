#!/usr/bin/python3
# -*- coding: utf-8 -*-

from s7_5 import calculate_price


def test_s7_5():
    assert calculate_price(343, 10) == 150
    assert calculate_price(381, 5) == 90
    assert calculate_price(473, 8) == 104
    assert calculate_price(485, 50) == 550
    assert calculate_price(0, 0) == 0
