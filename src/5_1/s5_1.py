#!/usr/bin/python3
# -*- coding: utf-8 -*-

def hello_world(name: str) -> str:
    return 'Привет, {name}!'.format(name=name)


def user_imput():
    name = input('Как тебя зовут?')
    return hello_world(str(name))
