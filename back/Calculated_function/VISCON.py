import numpy as np
from input_data import *

def VISCON(ci, cpi, tr):
    global vsa, vsb, vsc, emi, ns, rg
    r = rg
    t = tr / 1.8
    alogt = np.log(t)

    amufac = 2.205e-3 / 3.28e-2 / 32.17
    xi = np.zeros(ns)
    amui = np.zeros(ns)
    for n in range(ns):
        xi[n] = ci[n] / emi[n]
        amui[n] = np.exp(vsc[n]) * t ** (vsa[n] * alogt + vsb[n]) * amufac

    amu = 0
    akay = 0
    for n in range(ns):
        akayi = amui[n] / emi[n] * (cpi[n] * emi[n] / r + 1.25) * r

        fac = 0
        for j in range(ns):
            phi = (1 + np.sqrt(amui[n] / amui[j]) * (emi[j] / emi[n]) ** 0.25) ** 2 / np.sqrt(8) / (1 + emi[n] / emi[j]) ** 0.5
            fac += xi[j] * phi
        fac = xi[n] / fac

        amu += amui[n] * fac
        akay += akayi * fac

    return amu, akay
