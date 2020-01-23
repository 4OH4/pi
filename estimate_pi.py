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
    coords = 2 * np.random.random((n, 2)) - 1

    # Area of square
    area_square = 4

    # Estimate area of circle
    radius = 1
    distance = np.sum(coords**2, axis=1)**0.5
    points_in_circle = distance <= radius
    prob_point_in_circle = np.sum(points_in_circle) / n
    area_circle = prob_point_in_circle * area_square

    # Estimate pi
    pi_hat = area_circle / radius**2
    print('Estimate of pi: %f' % pi_hat)


if __name__ == "__main__":

    exp = 6
    repeats = 10

    print(f'Estimating pi using random sampling, n={10**exp}')

    wrapper_func = lambda : run(exp)

    duration = timeit.timeit(wrapper_func, number=repeats)
    
    print(f'{repeats} repeats: {duration} secs = {duration/repeats} secs/run')


