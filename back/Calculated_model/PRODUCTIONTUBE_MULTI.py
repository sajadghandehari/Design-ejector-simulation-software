import math
import numpy
from Calculated_function.HCP import *
from Calculated_function.intrp3 import *
from Calculated_function.VISCON import *
from Calculated_function.INCOMPRESIBLE import *
import sys
sys.path.append('/path/to/Calculated_function')


def PRODUCTIONTUBE_MULTI(press_s, t22, orifice_d, d_av, tube_d, ppc, tpc, q_t, press_amb, temp_amb, depth, temp_grad1, teta, g, rol, gama_gas, wc):

    global tmptab, htab01, htab02, htab03, htab04, htab05, htab06, ntab, n_tab
    global cptab01, cptab02, cptab03, cptab04, cptab05, cptab06, delhif, ns, n_species
    global vsa, vsb, vsc, emi, rg, xx
    global number, x_stem, tension_b, pd1, rr

    ll = depth * 1000
    delta_l = ll / 100
    length = delta_l
    p1 = press_s
    t1 = t22
    t2 = t1 + temp_grad1 * delta_l / 1000
    tav = 0.5 * (t1 + t2)
    p2 = press_s
    beta = orifice_d / d_av
    pu = p2
    pr = pu / ppc
    tr = t2 / tpc
    temp_s = t22
    # print('\n\n\n P1 :', p1, '\n\n\n')

    if pr > 1:
        pr = 1

    if tr > 1:
        tr = 1

    z2 = INCOMPRESIBLE(pr, tr)
    rou = 2.7 * pu / (z2 * t2)
    q_gsc = q_t
    q_mm = q_gsc * 14.7 / press_amb * (temp_amb) / 520
    pr = p2 / ppc
    tr = t2 / tpc

    if pr > 1:
        pr = 1

    if tr > 1:
        tr = 1

    z2 = INCOMPRESIBLE(pr, tr)
    t2 = t1 + temp_grad1 * length / 1000
    vm = 60 * 0.001 * q_gsc * t2 / (d_av ** 2 * press_amb)
    cpii, hii, hfac = HCP(t2)
    enthalpy = 0
    s_heat = 0

    for i in range(n_species):
        s_heat += cpii[i] * xx[i]
        enthalpy += hii[i] * xx[i]

    amu, akay = VISCON(xx, cpii, t2)

    if p2 < 1500:
        miu = 0.001 * math.exp(-0.001 * p2)
    else:
        miu = 0.001 * math.exp(-0.001 * 1500)

    lan_l = (amu / miu * rol / rou) ** 0.5
    lan_g = 1 - lan_l
    q_g = lan_g * q_t
    q_l = lan_l * q_t
    rgas = lan_g / lan_l / 5.61
    landag1 = lan_g
    landal1 = lan_l
    gama_gas = landag1 * gama_gas
    amu = amu * landag1 + miu * landal1
    ro = 2.7 * pu / (z2 * t2) * landag1
    re = ro * vm * tube_d / (amu * g)

    if re < 2400:
        ff = 16 / re
    else:
        ff = numpy.real((1 / (2.28 - 4 / math.log(2.72) *
                        math.log(0.0006 / (d_av / 12) + 21.25 / re ** 0.9))) ** 2)

    while length < ll:
        eps6 = 1
        t2 = t1 + temp_grad1 * delta_l / 1000

        # print('\n length :', length)
        # print(' ll :', ll, '\n')

        while abs(eps6) > 0.1:
            vm = 60 * 0.001 * q_gsc * t2 / (d_av ** 2 * press_amb)
            cpii, hii, hfac = HCP(t2)
            enthalpy = 0
            s_heat = 0

            for i in range(n_species):
                s_heat += cpii[i] * xx[i]
                enthalpy += hii[i] * xx[i]

            amu, akay = VISCON(xx, cpii, t2)

            if p2 < 1500:
                miu = 0.001 * math.exp(-0.001 * p2)
            else:
                miu = 0.001 * math.exp(-0.001 * 1500)

            lan_l = (amu / miu * rol / rou) ** 0.5
            lan_g = 1 - lan_l
            q_g = lan_g * q_t
            q_l = lan_l * q_t
            rgas = lan_g / lan_l / 5.61
            landag1 = lan_g
            landal1 = lan_l
            gama_gas = landag1 * gama_gas
            amu = amu * landag1 + miu * landal1
            ro = 2.7 * pu / (z2 * t2) * landag1
            re = ro * vm * tube_d / (amu * g)

            if re < 2400:
                ff = 16 / re
            else:
                ff = numpy.real((1 / (2.28 - 4 / math.log(2.72) *
                                math.log(0.0006 / (d_av / 12) + 21.25 / re ** 0.9))) ** 2)

            pr = p1 / ppc
            tr = t1 / tpc

            if pr > 1:
                pr = 1

            if tr > 1:
                tr = 1

            z = INCOMPRESIBLE(pr, tr)
            z1 = z
            ii1 = (
                (p1 / (z1 * t1) - 2.082 * gama_gas * q_g ** 2 / (d_av ** 4 * p1))
                / (2.6665 * ff * q_g ** 2 / d_av ** 5 + math.cos(teta) * (p1 / (t1 * z1)) ** 2 / 1000)
            )
            ii2 = ii1
            eps = 1

            while abs(eps) > 0.1:
                vm = 60 * 0.001 * q_gsc * t2 / (d_av ** 2 * press_amb)
                cpii, hii, hfac = HCP(t2)
                enthalpy = 0
                s_heat = 0

                for i in range(n_species):
                    s_heat += cpii[i] * xx[i]
                    enthalpy += hii[i] * xx[i]

                amu, akay = VISCON(xx, cpii, t2)

                if p2 < 1500:
                    miu = 0.001 * math.exp(-0.001 * p2)
                else:
                    miu = 0.001 * math.exp(-0.001 * 1500)

                lan_l = (amu / miu * rol / rou) ** 0.5
                lan_g = 1 - lan_l
                q_g = lan_g * q_t
                q_l = lan_l * q_t
                rgas = lan_g / lan_l / 5.61
                landag1 = lan_g
                landal1 = lan_l
                p2 = p1 - 37.484 * gama_gas * delta_l / (ii1 + ii2)
                p2l = ((-math.cos(teta) * rol - ff * vm ** 2 * rol /
                       (2 * g * tube_d / 12)) * delta_l) / 144 + p1
                p2 = p2l * landal1 + p2 * landag1
                p2_est = p2
                p22 = p2
                pr = pu / ppc
                tr = t2 / tpc

                if pr > 1:
                    pr = 1

                if tr > 1:
                    tr = 1

                z2 = INCOMPRESIBLE(pr, tr)
                rou = 2.7 * pu / (z2 * t2) * landag1
                re = ro * vm * tube_d / (amu * g)

                if re < 2400:
                    ff = 16 / re
                else:
                    ff = numpy.real(
                        (1 / (2.28 - 4 / math.log(2.72) * math.log(0.0006 / (d_av / 12) + 21.25 / re ** 0.9))) ** 2)

                ii2 = ((p2 / (z2 * t2) - 2.082 * gama_gas * q_g ** 2 / (d_av ** 4 * p2)) /
                       (2.6665 * ff * q_g ** 2 / d_av ** 5 + math.cos(teta) * (p2 / (t2 * z2)) ** 2 / 1000))
                p2 = p1 - 37.484 * gama_gas * delta_l / (ii1 + ii2)
                p2l = ((-math.cos(teta) * rol - ff * vm ** 2 * rol /
                       (2 * g * tube_d / 12)) * delta_l) / 144 + p1
                p2 = p2l * landal1 + p2 * landag1
                p2_est = p2
                eps = p2 - p2_est
                p2_est = p2

            temp_grad = ((1.35 - 11.02 / tube_d ** 2 * math.log(q_t / (1000000 * 5.61)) + 1.5) /
                         (math.log((rgas * (0.0125 * (temp_s - 459))) / p2))) * 54 / 8

            # print("tube_d:", tube_d)
            # print("q_t:", q_t)
            # print("temp_s:", temp_s)
            # print("p2:", p2)
            # print("rgas:", rgas)
            # print("temp_grad:", temp_grad)

            t2est = t2
            t2 = temp_grad * delta_l / 1000 + t1
            eps6 = abs(t2 - t2est)
            temp_grad1 = temp_grad

        length = length + delta_l
        if type(p2) != int:
            p2 = p2[0]

        p22 = p2
        p1 = p2
        t1 = t2

    q_oil = (1 - wc) * q_l * 5.61
    q_water = wc * q_l * 5.61
    p_ex = p2
    temp_grad5 = temp_grad

    return vm, q_oil[0], q_water[0], q_g[0], p2, ff, temp_grad5
