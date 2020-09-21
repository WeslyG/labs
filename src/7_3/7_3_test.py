#!/usr/bin/python3
# -*- coding: utf-8 -*-

from s7_3 import number_is_even


def test_s7_3():
    assert number_is_even(7) is False
    assert number_is_even(6) is True
    assert number_is_even(0) is True
