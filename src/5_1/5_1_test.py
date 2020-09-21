#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
from s5_1 import user_imput


def test_right_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Вася'))
    assert user_imput() == 'Привет, Вася!'


def test_broken_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Петя'))
    assert user_imput() != 'Привет, Вася!'
