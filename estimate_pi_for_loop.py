# -*- coding: utf-8 -*-
"""

Estimate pi using random sampling

@author: 4oh4
Created 23/01/22

"""

import timeit

import numpy as np


def run(exp=6):
    # Run random sampling and calculate estimate of pi
    if exp>9:
        print('Limiting scale to 10^9 data points')
        exp = 9

    # Generate random data in (-1, 1) space
    n = 10**exp
    x = 2 * np.random.random(n) - 1
    y = 2 * np.random.random(n) - 1

    # Area of square
    area_square = 4

    # Estimate area of circle
    radius = 1

    points_in_circle = 0
    for i in range(n):

        distance = (x[i]**2 + y[i]**2)**0.5

        if distance < radius:
            points_in_circle += 1

    prob_point_in_circle = points_in_circle / n
    area_circle = prob_point_in_circle * area_square

    # Estimate pi
    pi_hat = area_circle / radius**2
    print('Estimate of pi: %f' % pi_hat)


if __name__ == "__main__":
    
    exp = 6
    repeats = 10

    print(f'Estimating pi using random sampling (non-optimised), n={10**exp}')

    wrapper_func = lambda : run(exp)

    duration = timeit.timeit(wrapper_func, number=repeats)
    
    print(f'{repeats} repeats: {duration} secs = {duration/repeats} secs/run')