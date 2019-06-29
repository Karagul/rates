import numpy as np


# Pseudo-random number generators for simulations
def rand_uniform(n=1, method='lgm', seed=10, shuffle=True):
    if method == 'lgm':
        rand = np.zeros(n + 1)
        rand[0] = seed

        a = 5 ** 5
        b = 0
        m = 2 ** 31 - 1

        for toss in range(1, n):
            rand[toss] = (a * rand[toss - 1] + b) % m

        rand = (rand[1:] + .5) / m
    else:
        rand = np.nan

    if shuffle is True:
        np.random.shuffle(rand)

    return rand


def rand_normal(n=1, mean=0, var=1, seed=10, shuffle=True, method='box-muller'):
    if method == 'box-muller':
        # Two columns of uniformly distributed random numbers
        uni = rand_uniform(n * 2, seed=seed).reshape(-1, 2)
        z = np.sqrt(-2 * np.log(uni[:, 0])) * np.cos(2 * np.pi * uni[:, 1])

        # From standard-normal to normal
        rand = (z + mean) * np.sqrt(var)
    else:
        rand = np.nan

    if shuffle is True:
        np.random.shuffle(rand)

    return rand
