#! /usr/bin/env python

"""
File: sin_deriv.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: B.2
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Plots stuff
"""

import numpy as np
import matplotlib.pyplot as plt


def sin_func(x):
    return np.sin(1/float(x))
def run(n, e):
    y_val = []
    x_val = np.linspace(0, 2 * np.pi, n)
    for elem in x_val:
        elem += e
        y_val.append(sin_func(elem))
    plt.plot(x_val, y_val)
    y_val1 = []
    x_val1 = np.linspace(0, 2 * np.pi, n+10)
    for elem in x_val1:
        elem += e
        y_val1.append(sin_func(elem))
    plt.plot(x_val, y_val)
    plt.show()
def run2(e):
    n = 2
    error = 1
    while(error > 0.1):
        y_val = []
        x_val = np.linspace(0, 2 * np.pi, n)
        for elem in x_val:
            elem += e
            y_val.append(sin_func(elem))
        y_val1 = []
        x_val1 = np.linspace(0, 2 * np.pi, n+10)
        for elem in x_val1:
            elem += e
            y_val1.append(sin_func(elem))
        error1 = []
        for i in xrange(len(y_val)):
            error1.append(abs(y_val[i] - y_val1[i]))
        error = max(error1)
        n += 1
    print n