#! /usr/bin/env python

"""
File: integrate_exp.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: HW 5
Date: March 18
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description:
"""
import numpy as np
import matplotlib.pyplot
def trapezoidal(f, a, b, n):
    """Trapezoidal integration via iteration."""
    h = (b-a)/float(n)
    I = f(a) + f(b)
    for k in xrange(1, n, 1):
        x = a + k*h
        I += 2*f(x)
    I *= h/2
    return I
def func(x):
    return np.exp(-1 * (x ** 2))
def part_a():
    x = np.linspace(-10,10,1001)
    y = func(x)
    plt.plot(x,y)
    plt.show()
    print "The plot is symmetric"
def run():
    n = [100,200,300,400,500]
    L = [2,4,6,8,10]

    for elem_n in n:
        for elem_L in L:
            I = trapezoidal(func, 0, elem_L, elem_n)
            I *= 2
            print "I: " + str(I) + ", Error: " + str(I - np.sqrt(np.pi)),
        print " "