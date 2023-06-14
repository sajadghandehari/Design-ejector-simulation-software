import sys
sys.path.append('/path/to/Calculated_function')


from back.Calculated_function.INCOMPRESIBLE import *
from back.Calculated_function.VISCON import *
from back.Calculated_function.intrp3 import *
from back.Calculated_function.HCP import *

import math
import numpy


def ANALUAS_SINGLE(self, orifice_d1, d_av, depth, p_input, temp_s, casing_d, tube_d, temp_grad, pt, teta, ppc, tpc, gama_gas, g, area_p):
    global tmptab, htab01, htab02, htab03, htab04, htab05, htab06, ntab, n_tab
    global cptab01, cptab02, cptab03, cptab04, cptab05, cptab06, delhif, ns, n_species
    global vsa, vsb, vsc, emi, rg, xx 
    global number, x_stem, tension_b, pd1, rr

    orifice_d = orifice_d1  
    eps11 = 1

    while eps11 > 0.01:
        # print('\n\n',orifice_d, '\n\n')
        # print('\n\n',orifice_d1, '\n\n')

        q_t = 0.1
        t_w = 600
        eps2 = 10.0
        a_orif = 3.14 * (orifice_d/12)**2 / 4
        a_analus = 3.14 * (d_av/12)**2 / 4


        while abs(eps2) > 0.1:
        
            ll = depth * 1000
            delta_l = ll / 100
            length = delta_l
            p1 = p_input
            t1 = temp_s
            p2 = p1
            if p2 > (pt / 0.546):
                pu = pt / 0.546
            else:
                pu = p2
            d2 = casing_d
            d1 = tube_d


            while length < ll:
                t2 = t1 - temp_grad * delta_l / 1000
                tav = 0.5 * (t1 + t2)
                pr = (p2 + p1) / 2 / ppc
                tr = (t1 + t2) / 2 / tpc
                if pr > 1:
                    pr = 1.0
                if tr > 1:
                    tr = 1.0
                beta = orifice_d / d_av
                pd = pt
                pr = p2 / ppc
                tr = t2 / 2 / tpc
                if pr > 1:
                    pr = 1.0
                if tr > 1:
                    tr = 1.0
                [z2] = INCOMPRESIBLE(pu / ppc, t2 / tpc)
                vg = 60 * 0.001 * q_t * z2 * t2 / (orifice_d ** 2 * p1)
                rou = 2.7 * pu / (z2 * t2)
                [cpii, hii, hfac] = HCP(self, t2)
                entalpy = 0
                s_heat = 0
                for i in range(self.n_species):
                    s_heat = s_heat + cpii[i] * self.xx[i]
                    entalpy = entalpy + hii[i] * self.xx[i]
                [amu, akay] = VISCON(self, self.xx, cpii, t2)
                re = 2 / 6.7 * q_t * gama_gas / (amu * 32 * d_av)
                if re < 2400:
                    ff = 16 / re
                else:
                    ff = numpy.real((1 / (2.28 - 4 / math.log(2.72) * math.log(0.0006 / (d_av / 12) + 21.25 / re ** 0.9))) ** 2)
                z1 = z2
                ii1 = ((p1 / (z1 * t1) - 2.082 * gama_gas * q_t ** 2 / (d_av ** 4 * p1)) / (
                            2.6665 * ff * q_t ** 2 / d_av ** 5 - math.cos(teta) * (p1 / (t1 * z1)) ** 2 / 1000))
                ii2 = ii1
                p2 = p1 - 37.484 * gama_gas * delta_l / (ii1 + ii2)
                eps = 1


                while abs(eps) > 0.1:
                    p2_est = p2
                    pr = pu / ppc
                    tr = t2 / tpc
                    if pr > 1:
                        pr = 1.0
                    if tr > 1:
                        tr = 1.0
                    z2 = INCOMPRESIBLE(pu / ppc, t2 / tpc)
                    re = 2 / 6.7 * q_t * gama_gas / (amu * 32 * d_av)
                    if re < 2400:
                        ff = 16 / re
                    else:
                        ff = numpy.real((1 / (2.28 - 4 / math.log(2.72) * math.log(0.0006 / (d_av / 12) + 21.25 / re ** 0.9))) ** 2)
                    ii2 = ((p2 / (z2 * t2) - 2.082 * gama_gas * q_t ** 2 / (d_av ** 4 * p2)) / 
                        (2.6665 * ff * q_t ** 2 / d_av ** 5 - math.cos(teta) * (p2 / (t2 * z2)) ** 2 / 1000))
                    p2 = p1 - 37.484 * gama_gas * delta_l / (ii1 + ii2)
                    eps = abs(p2 - p2_est)



                length = length + delta_l
                p1 = p2
                t1 = t2






            gama = s_heat / (s_heat - self.rg * 1545 / 10.5)
            beta = orifice_d / d_av
            cd = (0.598 + 0.468 * (beta ** 4 + 10 * beta ** 12)) * (1 - beta ** 4) ** 0.5 \
                + (0.87 + 8.1 * beta ** 4) * ((1 - beta ** 4) / 10 ** 6) ** 0.5
            qmax = 0.43 * (orifice_d) ** 2 / 64 * pu * 12 * 12 * (1 / (gama_gas * t2)) ** 0.5 * \
                (0.546 ** 1.538 - 0.546 ** 1.769) ** 0.5
            q_t1 = 1240.3 * a_orif * 144 * 0.9 * (pu * (pu - pd) / ((1 - beta ** 4) * z2 * t2 * gama_gas)) ** 0.5

            eps2 = abs(q_t1 - q_t)

            q_t = q_t1


        

        diff_tension = p2 - (1/(1-self.rr)*self.pd1 - self.rr/(1-self.rr)*pt)

        xstem = intrp3(diff_tension, self.tension_b, self.x_stem, self.number)
        d_pilot = (4*area_p/3.14)**0.5
        area_p_eq = 3.14 * d_pilot * xstem
        d_orif = (4 * area_p_eq / 3.14)**0.5

        if d_orif < orifice_d1:
            eps11 = abs(d_orif - orifice_d)
            orifice_d = d_orif
        else:
            orifice_d = orifice_d1
            eps11 = 0




    return vg, p2, t2, ff, q_t, orifice_d, xstem