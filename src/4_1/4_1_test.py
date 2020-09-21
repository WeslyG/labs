#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pytest import approx
from s4_1 import convert_temperature


def test_books_value():
    assert int(convert_temperature(232.778)) == 451


def test_zero():
    assert convert_temperature(0) == 32


def test_float():
    assert convert_temperature(36.6) == approx(97.88)
