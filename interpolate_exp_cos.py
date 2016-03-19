#! /usr/bin/env python

"""
File: interpolate_exp_cos.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: B.1
Date: March 18
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Interpolates a function's points
"""

from numpy import *
import sys


def fx(x):
    return exp(-1* (x ** 2)) * cos(2 * pi * x)
def run():
    def S_k(k):
        return s[k] + ((s[k+1] - s[k])/(x[k+1] - x[k]))*(xp - x[k])
    xp = -0.45
    n_values = [2.0, 4.0, 8.0, 16.0]
    for n in n_values:
        h = 2/n
        x = linspace(-1, 1, n+1)
        s = fx(x)
        k = int(xp/h)
        print 'q = ' + str(n)
        print 'Approximation of f(%s): ' % xp, S_k(k)
        print 'Exact value of f(%s): ' % xp, sin(xp)
        print 'Eror in approximation: ', sin(xp) - S_k(k)
        print