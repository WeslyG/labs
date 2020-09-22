#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import pytest
from s9_4 import guess_number, get_random_int


def test_s9_4(capsys, mocker, monkeypatch):
    mocker.patch('s9_4.get_random_int', return_value=5)
    monkeypatch.setattr('sys.stdin', io.StringIO('1\n3\n5'))
    guess_number()
    stdout = capsys.readouterr()
    assert stdout.out == 'Угадай число от 1 до 10: Повторите еще раз: Повторите еще раз: Победа!\n'


def test_s9_4_broken_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO('a\n'))
    with pytest.raises(SystemExit) as wrapped_exception:
        guess_number()
    stdout = capsys.readouterr()
    assert stdout.out == "Угадай число от 1 до 10: Ошибка: Пожалуйста введите число!\n"
    assert wrapped_exception.value.code == 1
