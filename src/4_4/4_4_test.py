#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pytest import approx
from s4_4 import average_of_tree_number


def test_pass():
    assert average_of_tree_number() == 10
    assert average_of_tree_number(one=7.6) == approx(7.53, rel=1e-2)
