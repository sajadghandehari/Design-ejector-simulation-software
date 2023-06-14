import numpy as np
from back.Calculated_function.intrp3 import *


def INCOMPRESIBLE(pr, tr, condition=False):
    n1 = 6
    n2 = 8
    tr1 = 0.05
    prr = np.array([0, 0.5, 1, 2, 4, 6, 8, 10])
    z1 = np.array([1, 0.58, 0.28, 0.4, 0.53, 0.6, 0.78, 0.9])
    tr2 = 0.8
    z2 = np.array([1, 0.77, 0.56, 0.54, 0.6, 0.7, 0.8, 0.9])
    tr3 = 2
    z3 = np.array([1, 0.83, 0.68, 0.63, 0.65, 0.72, 0.8, 0.9])
    tr4 = 3.5
    z4 = np.array([1, 0.85, 0.77, 0.7, 0.71, 0.75, 0.82, 0.91])
    tr5 = 6
    z5 = np.array([1, 0.92, 0.9, 0.88, 0.85, 0.88, 0.91, 0.95])
    tr6 = 15
    z6 = np.array([1, 1, 1, 1, 1, 1, 1, 1])

    if condition:
        zz1 = np.array(intrp3(pr, prr, z1, n2))
        zz2 = intrp3(pr, prr, z2, n2)
        zz3 = intrp3(pr, prr, z3, n2)
        zz4 = intrp3(pr, prr, z4, n2)
        zz5 = intrp3(pr, prr, z5, n2)
        zz6 = intrp3(pr, prr, z6, n2)
        trr = np.array([tr1, tr2, tr3, tr4, tr5, tr6])
        
        zz = np.stack((zz1, zz2, zz3, zz4, zz5, zz6))
        z = np.array([intrp3(tr, trr, zz, n1)])

    else:
        zz1 = np.array([intrp3(pr, prr, z1, n2)])
        zz2 = np.array([intrp3(pr, prr, z2, n2)])
        zz3 = np.array([intrp3(pr, prr, z3, n2)])
        zz4 = np.array([intrp3(pr, prr, z4, n2)])
        zz5 = np.array([intrp3(pr, prr, z5, n2)])
        zz6 = np.array([intrp3(pr, prr, z6, n2)])
        trr = np.array([tr1, tr2, tr3, tr4, tr5, tr6])

        zz = np.concatenate((zz1, zz2, zz3, zz4, zz5, zz6))
        z = np.array([intrp3(tr, trr, zz, n1)])

    return z
