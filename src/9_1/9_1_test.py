#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import pytest
from s9_1 import square_of_triangle


def test_s9_1(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('3\n4\n5'))
    square_of_triangle()
    stdout = capsys.readouterr()
    assert stdout.out == 'Введите сторону a: Введите сторону b: Введите сторону c: Площадь = 6.0\n'


def test_s9_1_broken_input(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a\ne\nb'))
    with pytest.raises(SystemExit) as wrapped_exception:
        square_of_triangle()
    stdout = capsys.readouterr()
    assert stdout.out == "Введите сторону a: Ошибка: Пожалуйста введите число!\n"
    assert wrapped_exception.value.code == 1
