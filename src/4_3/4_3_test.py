#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pytest import approx
from s4_3 import average_of_tree_number


def test_pass():
    assert average_of_tree_number(15, 30, 15) == 20
    assert average_of_tree_number(0, 0, 0) == 0
    assert average_of_tree_number(-20, 30, -50) == approx(-13.3, rel=1e-2)
