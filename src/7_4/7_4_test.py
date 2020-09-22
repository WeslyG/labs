#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pytest import approx
from s7_4 import custom_function


def test_s7_4():
    assert custom_function(-5) == 4
    assert custom_function(6) == 4
    assert custom_function(0.33) == approx(0.1089)
    assert custom_function(-2.2) == approx(4.84)
