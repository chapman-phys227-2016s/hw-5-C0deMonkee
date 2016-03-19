#! /usr/bin/env python

"""
File: diff_functions.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: B. 8
Date: March 18
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description:
"""
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.log(x + 1/100.0)
def g(x):
    return np.cos(np.exp(10*x))
def h(x):
    return x ** x
def df(x):
    return 1/(x+1/100.0)
def dg(x):
    return -10 * np.exp(10*x) * np.sin(np.exp(10*x))
def dh(x):
    return np.log(x)*x**x + x*x**(x-1)
def diff(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = np.zeros(len(x))
    z = np.zeros(len(x))
    h = (b-a)/float(n)
    for i in xrange(len(x)):
        y[i] = f(x[i])
    for i in xrange(len(x)-1):
        z[i] = (y[i+1] - y[i])/h
    z[n] = (y[n] - y[n-1])/h
    return y, z
def run():
    x_space = np.linspace(1/1000.0, 1, 1001)
    numerical_f = diff(f,1/1000.0, 1, 1000)[1]
    numerical_g = diff(g,1/1000.0, 1, 1000)[1]
    numerical_h = diff(h,1/1000.0, 1, 1000)[1]
    actual_f = df(x_space)
    actual_g = dg(x_space)
    actual_h = dh(x_space)
    plt.plot(x_space, numerical_f)
    plt.plot(x_space, actual_f)
    plt.show()
    plt.clf()
    plt.plot(x_space, numerical_g)
    plt.plot(x_space, actual_g)
    plt.show()
    plt.clf()
    plt.plot(x_space, numerical_h)
    plt.plot(x_space, actual_h)
    plt.show()
    plt.clf()