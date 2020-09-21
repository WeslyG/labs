#!/usr/bin/python3
# -*- coding: utf-8 -*-

from s7_2 import maximum_from_two_numbers_recursion


def test_s7_2():
    assert maximum_from_two_numbers_recursion(15, 2) == 15
    assert maximum_from_two_numbers_recursion(6, 200) == 200
    assert maximum_from_two_numbers_recursion(0, 0) == 0
