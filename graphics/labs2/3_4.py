#!/usr/bin/python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import interp1d

N = 8
A = 1


def get_period() -> float:
    # ((2 * math.pi) / (2 * math.pi * N))
    return (1 / N)


def linear_interpolation(t):
    return start * t + end
    # P1(x) = ax + b


def base_function(t: float) -> float:
    w = 2 * math.pi * N
    fi = (2 * math.pi) / N
    return A * math.sin(w * t + fi)


def generate_range(start: int, end: int, step: float) -> list:
    return np.arange(start, end, step).tolist()


def generate_function_list(data: list) -> list:
    function_output = []
    for i in data:
        function_output.append(base_function(i))
    return function_output


def get_step_discret(count: int) -> list:
    period = get_period()
    return generate_range(0, 2 * period, period / count)

# X
x_2 = get_step_discret(2)
x_4 = get_step_discret(4)
x_8 = get_step_discret(8)
x_16 = get_step_discret(16)
x_source = get_step_discret(128)

# Y
y_2 = generate_function_list(x_2)
y_4 = generate_function_list(x_4)
y_8 = generate_function_list(x_8)
y_16 = generate_function_list(x_16)
y_source = generate_function_list(x_source)

f_2 = interp1d(x_2, y_2)
f_4 = interp1d(x_4, y_4)
f_8 = interp1d(x_8, y_8)
f_16 = interp1d(x_16, y_16)

f_cubic_2 = interp1d(x_2, y_2, kind='cubic')
f_cubic_4 = interp1d(x_4, y_4, kind='cubic')
f_cubic_8 = interp1d(x_8, y_8, kind='cubic')
f_cubic_16 = interp1d(x_16, y_16, kind='cubic')

xnew_2 = np.linspace(0, x_2[3], num=256)
xnew_4 = np.linspace(0, x_4[7], num=256)
xnew_8 = np.linspace(0, x_8[15], num=256)
xnew_16 = np.linspace(0, x_16[31], num=256)

plt.figure()
# 2
for_2 = plt.subplot(231)
for_2.title.set_text('2 точки в периоде')
plt.plot(x_2, y_2, 'o')
plt.plot(xnew_2, f_2(xnew_2), '-')
plt.plot(xnew_2, f_cubic_2(xnew_2), '--')
plt.legend(['discret', 'linear', 'cubic'], loc='best')

# 4
for_4 = plt.subplot(232)
for_4.title.set_text('4 точки в периоде')
plt.plot(x_4, y_4, 'o')
plt.plot(xnew_4, f_4(xnew_4), '-')
plt.plot(xnew_4, f_cubic_4(xnew_4), '--')
plt.legend(['discret', 'linear', 'cubic'], loc='best')

# 8
for_8 = plt.subplot(233)
for_8.title.set_text('8 точек в периоде')
plt.plot(x_8, y_8, 'o')
plt.plot(xnew_8, f_8(xnew_8), '-')
plt.plot(xnew_8, f_cubic_8(xnew_8), '--')
plt.legend(['discret', 'linear', 'cubic'], loc='best')

# 16
for_16 = plt.subplot(234)
for_16.title.set_text('16 точек в периоде')
plt.plot(x_16, y_16, 'o')
plt.plot(xnew_16, f_16(xnew_16), '-')
plt.plot(xnew_16, f_cubic_16(xnew_16), '--')
plt.legend(['discret', 'linear', 'cubic'], loc='best')

plt.show()
