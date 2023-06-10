import matplotlib.pyplot as plt
from Calculated_model.ANALUAS_SINGLE import *
from Calculated_model.PRODUCTIONTUBE_MULTI import *

import numpy as np


# Initializing arrays for results
q_t = np.zeros(n_p)
vg = np.zeros(n_p)
p_inj = np.zeros(n_p)

t_w = np.zeros(n_p)
t22 = np.zeros(n_p)
pvo = np.zeros(n_p)
p_ex = np.zeros(n_p)
q_oil = np.zeros(n_p)
q_water = np.zeros(n_p)

q_g = np.zeros(n_p)
vmm = np.zeros(n_p)
ff = np.zeros(n_p)

fl2 = np.zeros(n_p)
xstemb = np.zeros(n_p)
d_orif = np.zeros(n_p)

for ij in range(n_p):
    orifice_d = midata[1, 8]
    eps10 = 1
    print('ij: ', ij)
    while (eps10 > 0.1):
        teta = teta * 0.0174
        map = 0
        rg = 0
        for i in range(n_species):
            map = map + map1[i] * xx[i]
            rg = rg + rgrg[i] * xx[i]

        gama_gas = map / 29
        tpc = 170.491 + 307.344 * gama_gas
        ppc = 709.604 - 58.718 * gama_gas
        row = 71
        gapi = 20
        wc = 0.1
        ro = 57.0
        rol = wc * row + (1 - wc) * ro
        g = 32.2
        t_w[ij] = 600
        pvo[ij] = 1 / (1 - rr) * pd1 - rr / (1 - rr) * pt[ij] + st
        pd = pt[ij]

        p_input1 = p_input[ij]
        temp_s1 = temp_s[ij]
        temp_grad2 = temp_grad[ij]
        pt2 = pt[ij]
        orifice_d1 = orifice_d

        vg2, p2, t2, ff2, q_t2, orifice_d, xstem = ANALUAS_SINGLE(
            orifice_d1, d_av, depth, p_input1, temp_s1, casing_d,
            tube_d, temp_grad2, pt2, teta, ppc, tpc, gama_gas, g, area_p
        )

        q_t[ij] = q_t2
        vg[ij] = vg2
        p_inj[ij] = p2

        t22[ij] = t2
        ff[ij] = ff2
        coff1 = 141.5 / (131.5 + gapi) * (1 - wc)
        coff2 = wc + coff1
        g = 32.2
        xstemb[ij] = xstem

        d_orif[ij] = orifice_d

        press_s = pt[ij]  # gas pressure at surface per psi
        temp_grad1 = temp_grad[ij]
        tin = t22[ij]

        vm, q_oo, q_ww, q_gg, p2e, ff2, temp_grad5 = PRODUCTIONTUBE_MULTI(
            press_s, tin, orifice_d, tube_d, tube_d, ppc, tpc, q_t2, press_amb,
            temp_amb, depth, temp_grad1, teta, g, rol, gama_gas, wc
        )

        vmm[ij] = vm
        p_ex[ij] = p2e
        q_oil[ij] = q_oo
        q_water[ij] = q_ww
        q_g[ij] = q_gg
        fl2[ij] = ff2
        eps10 = abs(temp_grad5 - temp_grad1)
        temp_grad[ij] = temp_grad5

    if pvo[ij] > p_inj[ij]:
        print(p_inj[ij])
        print('the operating valve not opened at this pressure surface(psig)=')
        print(ij)
        print(p_input[ij])
        break


# plot injection pressure from operating valve vs. gas surface pressure
plt.figure(1)
plt.plot(p_input.flatten(), p_inj.flatten())
plt.grid(True)
plt.title('injection pressure from operating valve PER gas surface pressure')
plt.ylabel('p-gas-inj(psig)')
plt.xlabel('p-gas-surf(psig)')


# plot exhuast pressure from production tube vs. gas surface pressure
plt.figure(2)
plt.plot(p_input.flatten(), p_ex.flatten())
plt.grid(True)
plt.title('exhaust pressure from production tube PER gas surface pressure')
plt.ylabel('p-mixture-ex(psig)')
plt.xlabel('p-gas-surf(psig)')

# plot gas flow rate injected from operating valve vs. gas surface pressure
plt.figure(3)
plt.plot(p_input.flatten(), q_t.flatten())
plt.grid(True)
plt.title('gas flow rate injected from operating valve PER gas surface pressure')
plt.ylabel('q-gas(Mscf/D)')
plt.xlabel('p-gas-surf(psig)')

# plot oil flow rate vs. gas surface pressure
plt.figure(4)
plt.plot(p_input.flatten(), q_oil.flatten())
plt.grid(True)
plt.title('oil flow rate PER gas surface pressure')
plt.ylabel('q-o(Brd/D)')
plt.xlabel('p-gas-surf(psig)')

# plot water flow rate vs. gas surface pressure
plt.figure(5)
plt.plot(p_input.flatten(), q_water.flatten())
plt.grid(True)
plt.title('water flow rate PER gas surface pressure')
plt.ylabel('q-w(Brd/D)')
plt.xlabel('p-gas-surf(psig)')

# plot gas flow rate from production tube vs. gas surface pressure
plt.figure(6)
plt.plot(p_input.flatten(), q_g.flatten())
plt.grid(True)
plt.title('gas flow rate from production tube PER gas surface pressure')
plt.ylabel('q-gas(Mscf/D)')
plt.xlabel('p-gas-surf(psig)')

# plot gas velocity from orifice vs. gas surface pressure
plt.figure(7)
plt.plot(p_input.flatten(), vg.flatten())
plt.grid(True)
plt.title('gas velocity from orifice PER gas surface pressure')
plt.ylabel('v-g(ft/s)')
plt.xlabel('p-gas-surf(psig)')

# plot multiphase velocity from production tube vs. gas surface pressure
plt.figure(8)
plt.plot(p_input.flatten(), vmm.flatten())
plt.grid(True)
plt.title('multi-phase velocity from production tube PER gas surface pressure')
plt.ylabel('v-m(ft/s)')
plt.xlabel('p-gas-surf(psig)')

# plot gas friction from orifice vs. gas surface pressure
plt.figure(9)
plt.plot(p_input.flatten(), ff.flatten())
plt.grid(True)
plt.title('gas friction from orifice PER gas surface pressure')
plt.ylabel('f')
plt.xlabel('p-gas-surf(psig)')

# plot multiphase friction from production tube vs. gas surface pressure
plt.figure(10)
plt.plot(p_input.flatten(), fl2.flatten())
plt.grid(True)
plt.title('multi-phase friction from production tube PER gas surface pressure')
plt.ylabel('fl')
plt.xlabel('p-gas-surf(psig)')

# plot stem displacement vs. gas surface pressure
plt.figure(11)
plt.plot(p_input.flatten(), xstemb.flatten())
plt.grid(True)
plt.title('Stem displacement(inch) PER gas surface pressure')
plt.ylabel('x-stem(in)')
plt.xlabel('p-gas-surf(psig)')


plt.figure(12)
plt.plot(p_input.flatten(), d_orif.flatten())
plt.grid(True)
plt.title('minimum diameter of operating valve (inch) PER gas surface pressure')
plt.ylabel('orifice-dia (in)')
plt.xlabel('p-gas-surf (psig)')

plt.show()
