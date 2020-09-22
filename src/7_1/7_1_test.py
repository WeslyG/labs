#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import pytest
from s7_1 import ph_getter


def test_s7_1_apple(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('3.0'))
    ph_getter()
    stdout = capsys.readouterr()
    assert stdout.out == 'Введите значение PH(float): Яблочный сок\n'


def test_s7_1_shampoo(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('5.5'))
    ph_getter()
    stdout = capsys.readouterr()
    assert stdout.out == 'Введите значение PH(float): Шампунь\n'


def test_s7_1_soap(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('9.1'))
    ph_getter()
    stdout = capsys.readouterr()
    assert stdout.out == 'Введите значение PH(float): Мыло для рук\n'


def test_s7_1_more(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('10.0'))
    ph_getter()
    stdout = capsys.readouterr()
    assert stdout.out == 'Введите значение PH(float): Не найдено\n'


def test_s7_1_less(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1.0'))
    ph_getter()
    stdout = capsys.readouterr()
    assert stdout.out == 'Введите значение PH(float): Не найдено\n'


def test_s7_1_incorrect_input(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a'))
    with pytest.raises(SystemExit) as wrapped_exception:
        ph_getter()
    stdout = capsys.readouterr()
    assert stdout.out == "Введите значение PH(float): Ошибка: PH должен быть числом!\n"
    assert wrapped_exception.value.code == 1
