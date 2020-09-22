#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pytest import approx
from s9_3 import user_function


def test_s9_3():
    assert user_function(10) == approx(0.839, rel=1e-2)
