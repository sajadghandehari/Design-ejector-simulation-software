import matplotlib.pyplot as plt
from back.Calculated_model.ANALUAS_SINGLE import *
from back.Calculated_model.PRODUCTIONTUBE_MULTI import *
# from input_data import *
import pandas
import numpy as np


class Run():
    def __init__(self, progressBar):

        # print(progressBar.value())
        self.progressBar = progressBar

    def run(self, excle_address):

        midata = pandas.read_excel(
            excle_address, sheet_name='GLS_properties', header=None).values
        midata1 = pandas.read_excel(
            excle_address, sheet_name='gas properties', header=None).values
        midata2 = pandas.read_excel(
            excle_address, sheet_name='specific heat_gas', header=None).values
        midata3 = pandas.read_excel(
            excle_address, sheet_name='entalpy_gas', header=None).values
        midata4 = pandas.read_excel(
            excle_address, sheet_name='Bellows', header=None).values

        self.n_species = midata1[1, 0]  # The number of types of injected gas
        self.ns = self.n_species
        self.map1, self.xx, self.rgrg, self.delhif, self.vsa, self.vsb, self.vsc = [
        ], [], [], [], [], [], []

        for i in range(1, self.n_species+1):
            self.map1.append(midata1[i, 1])  # molocular wight of any species
            self.xx.append(midata1[i, 2])  # molaur fraction of any species
            # gas canstant for any species per psia-ft.3/(lb-mole)-°R
            self.rgrg.append(midata1[i, 3])
            self.delhif.append(midata1[i, 4])  # Formation Enthalpy(ft^2/sec^2)
            # Vsa (Coffiecient of viscosity equestion for any species
            self.vsa.append(midata1[i, 5])
            # Vsb (Coffiecient of viscosity equestion for any species
            self.vsb.append(midata1[i, 6])
            # Vsc (Coffiecient of viscosity equestion for any species
            self.vsc.append(midata1[i, 7])

        self.n_tab = midata2[1, 0]
        self.tmptab, self.cptab01, self.cptab02, self.cptab03, self.cptab04, self.cptab05, self.cptab06 = [
        ], [], [], [], [], [], []

        for i in range(1, self.n_species+1):
            self.tmptab.append(midata2[i, 1])
            self.cptab01.append(midata2[i, 2])
            self.cptab02.append(midata2[i, 3])
            self.cptab03.append(midata2[i, 4])
            self.cptab04.append(midata2[i, 5])
            self.cptab05.append(midata2[i, 6])
            self.cptab06.append(midata2[i, 7])

        self.ntab = midata3[1, 0]
        self.htab01, self.htab02, self.htab03, self.htab04, self.htab05, self.htab06 = [
        ], [], [], [], [], []

        for i in range(1, self.n_species+1):
            self.tmptab.append(midata3[i, 1])
            self.htab01.append(midata3[i, 2])
            self.htab02.append(midata3[i, 3])
            self.htab03.append(midata3[i, 4])
            self.htab04.append(midata3[i, 5])
            self.htab05.append(midata3[i, 6])
            self.htab06.append(midata3[i, 7])

        self.number = midata4[1, 0]
        self.x_stem, self.tension_b = [], []

        for i in range(1, self.number+1):
            self.x_stem.append(midata4[i, 1])
            self.tension_b.append(midata4[i, 2])

        temp_amb = midata[1, 0]
        press_amb = midata[1, 1]
        depth = midata[1, 2]
        pd = midata[1, 3]
        st = self.tension_b[0]
        area_b = midata[1, 5]
        area_p = midata[1, 6]
        tube_d = midata[1, 7]
        orifice_d = midata[1, 8]
        casing_d = midata[1, 9]
        teta = midata[1, 10]
        gapi = midata[1, 11]
        wc = midata[1, 12]
        n_p = int(midata[1, 13])

        p_input = np.zeros(n_p)
        pt = np.zeros(n_p)
        temp_s = np.zeros(n_p)

        # Filling in input data
        for k in range(1, n_p+1):
            p_input[k-1] = midata[k, 14]
            pt[k-1] = midata[k, 15]
            temp_s[k-1] = midata[k, 16]

        # Initializing constants
        temp_grad = np.array([-10.00]*15)
        press_res = np.array([14.7]*15)
        self.rr = area_p / area_b
        d_pipe = 5
        d_av = np.sqrt(-tube_d**2 + casing_d**2)
        teta *= 0.0174
        map = 0
        self.rg = 0

        self.emi = np.zeros(self.n_species)

        # Calculating constants
        for i in range(self.n_species):
            map += self.map1[i] * self.xx[i]
            self.rg += self.rgrg[i] * self.xx[i]
            self.emi[i] = self.map1[i]

        gama_gas = map / 29
        tpc = 170.491 + 307.344 * gama_gas
        ppc = 709.604 - 58.718 * gama_gas
        row = 71
        ro = 57.0
        rol = wc * row + (1 - wc) * ro
        g = 32.2
        self.pd1 = pd

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
            self.current_value = self.progressBar.value()
            if self.current_value < 100:
                self.progressBar.setValue(self.current_value + 3)

            while (eps10 > 0.1):
                teta = teta * 0.0174
                map = 0
                self.rg = 0
                for i in range(self.n_species):
                    map = map + self.map1[i] * self.xx[i]
                    self.rg = self.rg + self.rgrg[i] * self.xx[i]

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
                pvo[ij] = 1 / (1 - self.rr) * self.pd1 - self.rr / \
                    (1 - self.rr) * pt[ij] + st
                pd = pt[ij]

                p_input1 = p_input[ij]
                temp_s1 = temp_s[ij]
                temp_grad2 = temp_grad[ij]
                pt2 = pt[ij]
                orifice_d1 = orifice_d

                vg2, p2, t2, ff2, q_t2, orifice_d, xstem = ANALUAS_SINGLE(
                    self, orifice_d1, d_av, depth, p_input1, temp_s1, casing_d,
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
                    self, press_s, tin, orifice_d, tube_d, tube_d, ppc, tpc, q_t2, press_amb,
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

            self.current_value = self.progressBar.value()
            if self.current_value < 100:
                self.progressBar.setValue(self.current_value + 3)

            if pvo[ij] > p_inj[ij]:
                print(p_inj[ij])
                print('the operating valve not opened at this pressure surface(psig)=')
                print(ij)
                print(p_input[ij])
                break

        # Create a new figure and subplots for 3 pages, each with 4 figures
        fig, axs = plt.subplots(3, 4, figsize=(19, 9.5))

        # Flatten the axes array for easier indexing
        axs = axs.flatten()

        # Iterate over the figures and plot the data
        for i, ax in enumerate(axs):
            # Calculate the index of the current figure
            fig_index = i + 1

            # Plot the data for the current figure
            if fig_index == 1:
                ax.plot(p_input.flatten(), p_inj.flatten())
                ax.set_title('Injection Pressure from Operating Valve')
                ax.grid(True)
                ax.set_ylabel('p-gas-inj(psig)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 2:
                ax.plot(p_input.flatten(), p_ex.flatten())
                ax.set_title('Exhaust Pressure from Production Tube')
                ax.grid(True)
                ax.set_ylabel('p-mixture-ex(psig)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 3:
                ax.plot(p_input.flatten(), q_t.flatten())
                ax.set_title('Gas Flow Rate Injected from Operating Valve')
                ax.grid(True)
                ax.set_ylabel('q-gas(Mscf/D)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 4:
                ax.plot(p_input.flatten(), q_oil.flatten())
                ax.set_title('oil flow rate PER gas surface pressure')
                ax.grid(True)
                ax.set_ylabel('q-o(Brd/D)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 5:
                ax.plot(p_input.flatten(), q_water.flatten())
                ax.set_title('water flow rate PER gas surface pressure')
                ax.grid(True)
                ax.set_ylabel('q-w(Brd/D)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 6:
                ax.plot(p_input.flatten(), q_g.flatten())
                ax.set_title('Gas flow rate vs. gas surface pressure')
                ax.grid(True)
                ax.set_ylabel('q-gas(Mscf/D)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 7:
                ax.plot(p_input.flatten(), vg.flatten())
                ax.set_title('Orifice gas velocity vs. surface pressure')
                ax.grid(True)
                ax.set_ylabel('v-g(ft/s)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 8:
                ax.plot(p_input.flatten(), vmm.flatten())
                ax.set_title('Multiphase velocity vs. surface pressure')
                ax.grid(True)
                ax.set_ylabel('v-m(ft/s)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 9:
                ax.plot(p_input.flatten(), ff.flatten())
                ax.set_title('Friction from orifice vs. surface pressure')
                ax.grid(True)
                ax.set_ylabel('f')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 10:
                ax.plot(p_input.flatten(), fl2.flatten())
                ax.set_title('Multiphase friction vs. surface pressure')
                ax.grid(True)
                ax.set_ylabel('fl')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 11:
                ax.plot(p_input.flatten(), xstemb.flatten())
                ax.set_title('Stem displacement vs. surface pressure')
                ax.grid(True)
                ax.set_ylabel('x-stem(in)')
                ax.set_xlabel('p-gas-surf(psig)')
            elif fig_index == 12:
                ax.plot(p_input.flatten(), d_orif.flatten())
                ax.set_title('Minimum valve diameter vs. surface pressure')
                ax.grid(True)
                ax.set_ylabel('orifice-dia (in)')
                ax.set_xlabel('p-gas-surf(psig)')

        # Hide any unused subplots
        for i in range(len(axs), 12):
            axs[i].axis('off')

        # Adjust the spacing between subplots
        plt.tight_layout()

        # Display or save the figure
        plt.show()
