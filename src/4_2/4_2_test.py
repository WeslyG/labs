#!/usr/bin/python3
# -*- coding: utf-8 -*-

from s4_2 import perimeter_of_square, area_of_square


def test_perimetr():
    assert perimeter_of_square(5) == 20


def test_square():
    assert area_of_square(8) == 16


def test_square_zero():
    assert area_of_square(0) == 0


def test_perimetr_zero():
    assert area_of_square(0) == 0
