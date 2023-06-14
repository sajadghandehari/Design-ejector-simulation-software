import numpy as np
# from input_data import *

def VISCON(self, ci, cpi, tr):
    global vsa, vsb, vsc, emi, ns, rg
    r = self.rg
    t = tr / 1.8
    alogt = np.log(t)

    amufac = 2.205e-3 / 3.28e-2 / 32.17
    xi = np.zeros(self.ns)
    amui = np.zeros(self.ns)
    for n in range(self.ns):
        xi[n] = ci[n] / self.emi[n]
        amui[n] = np.exp(self.vsc[n]) * t ** (self.vsa[n] * alogt + self.vsb[n]) * amufac

    amu = 0
    akay = 0
    for n in range(self.ns):
        akayi = amui[n] / self.emi[n] * (cpi[n] * self.emi[n] / r + 1.25) * r

        fac = 0
        for j in range(self.ns):
            phi = (1 + np.sqrt(amui[n] / amui[j]) * (self.emi[j] / self.emi[n]) ** 0.25) ** 2 / np.sqrt(8) / (1 + self.emi[n] / self.emi[j]) ** 0.5
            fac += xi[j] * phi
        fac = xi[n] / fac

        amu += amui[n] * fac
        akay += akayi * fac

    return amu, akay
