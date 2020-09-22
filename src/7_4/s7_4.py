#!/usr/bin/python3
# -*- coding: utf-8 -*-

# import matplotlib.pyplot as plt
# import numpy as np


def custom_function(x: float) -> float:
    if (x > -2.4 and x < 5.7):
        return x*x
    else:
        return 4


# a = np.arange(-10, 10, 0.5).tolist()
# b = []
# for i in a:
#     b.append(custom_function(i))

# plt.plot(a, b)
# plt.ylabel('Function value')
# plt.xlabel('User input')
# plt.show()
