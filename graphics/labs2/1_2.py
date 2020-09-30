#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math

# Rоэффициенты из задания
N = 8
A = 1


def get_period() -> float:
    '''
    Возвращает период функции по формуле
    ((2 * math.pi) / (2 * math.pi * N))
    '''
    return (1 / N)


def base_function(t: float) -> float:
    w = 2 * math.pi * N
    fi = (2 * math.pi) / N
    return A * math.sin(w * t + fi)


def generate_range(start: int, end: int, step: float)-> list:
    return np.arange(start, end, step).tolist()


def generate_function_list(data: list) -> list:
    '''
    Возвращает по list (x) list(y)
    т.е результат работы функции на всем периоде
    '''
    function_output = []
    for i in data:
        function_output.append(base_function(i))
    return function_output


def get_step_discret(count: int) -> list:
    '''
    Возвращает количество точек, необходимое для дискретного сигнала
    '''
    period = get_period()
    return generate_range(0, 2 * period, period / count)


x_2 = get_step_discret(2)
x_4 = get_step_discret(4)
x_8 = get_step_discret(8)
x_16 = get_step_discret(16)
x_source = get_step_discret(128)

y_2 = generate_function_list(x_2)
y_4 = generate_function_list(x_4)
y_8 = generate_function_list(x_8)
y_16 = generate_function_list(x_16)
y_source = generate_function_list(x_source)

for_2 = plt.subplot(231)
for_2.title.set_text('2 точки')
plt.plot(x_source, y_source)
plt.plot(x_2, y_2)

for_4 = plt.subplot(232)
for_4.title.set_text('4 точки')
plt.plot(x_source, y_source)
plt.plot(x_4, y_4)

for_8 = plt.subplot(233)
for_8.title.set_text('8 точек')
plt.plot(x_source, y_source)
plt.plot(x_8, y_8)

for_16 = plt.subplot(234)
for_16.title.set_text('16 точек')
plt.plot(x_source, y_source)
plt.plot(x_16, y_16)

plt.show()
