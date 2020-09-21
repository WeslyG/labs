#!/usr/bin/python3
# -*- coding: utf-8 -*-

import io
import pytest
from s5_2 import main


def test_correct_user_input(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('1\n3\n5'))
    main()
    stdout = capsys.readouterr()
    assert stdout.out == "Введите первое число: Введите второе число: Введите третье число: Сумма введеных чисел: 9\nПроизведение введеных чисел: 15\n"


def test_non_number_input(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('a\ne\nb'))
    with pytest.raises(SystemExit) as wrapped_exception:
        main()
    stdout = capsys.readouterr()
    assert stdout.out == "Введите первое число: Введите второе число: Введите третье число: Ошибка: Пожалуйста введите число!\n"
    assert wrapped_exception.value.code == 1
