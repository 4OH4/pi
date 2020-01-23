# -*- coding: utf-8 -*-
"""

Benchmark vectorised and non-vectorised code in numpy, by 
estimating pi using random sampling

@author: 4oh4
Created 23/01/22

"""

import timeit

from estimate_pi import run as vectorised
from estimate_pi_for_loop import run as non_vectorised


def run_estimate(func):
    # Run the estimate and profile the execution time

    wrapper_func = lambda : func(exp)

    duration = timeit.timeit(wrapper_func, number=repeats)
    
    print(f'{repeats} repeats: {duration:0.3f} secs = {duration/repeats:0.4f} secs/run')

    return duration


if __name__ == "__main__":

    exp = 6
    num_rounds = 10
    repeats = 10  # per round

    vectorised_duration = []
    non_vectorised_duration = []

    for round in range(num_rounds):

        print(f'Round {round+1} of {num_rounds}:')

        print(f'Estimating pi using random sampling (vectorised), n={10**exp}')
        vectorised_duration.append(run_estimate(vectorised))

        print(f'Estimating pi using random sampling (non-vectorised), n={10**exp}')
        non_vectorised_duration.append(run_estimate(non_vectorised))

    mean = lambda x: sum(x)/len(x)

    print('Final results:')
    print(f'Vectorised implementation: {mean(vectorised_duration):0.3f} seconds ({min(vectorised_duration):0.3f} - {max(vectorised_duration):0.3f})')
    print(f'Non-vectorised implementation: {mean(non_vectorised_duration):0.3f} seconds ({min(non_vectorised_duration):0.3f} - {max(non_vectorised_duration):0.3f})')
