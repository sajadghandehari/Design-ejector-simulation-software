import pandas
import numpy as np


midata = pandas.read_excel(
    'back/input.xls', sheet_name='GLS_properties', header=None).values
midata1 = pandas.read_excel(
    'back/input.xls', sheet_name='gas properties', header=None).values
midata2 = pandas.read_excel(
    'back/input.xls', sheet_name='specific heat_gas', header=None).values
midata3 = pandas.read_excel(
    'back/input.xls', sheet_name='entalpy_gas', header=None).values
midata4 = pandas.read_excel(
    'back/input.xls', sheet_name='Bellows', header=None).values

n_species = midata1[1, 0]  # The number of types of injected gas
ns = n_species
map1, xx, rgrg, delhif, vsa, vsb, vsc = [], [], [], [], [], [], []


for i in range(1, n_species+1):
    map1.append(midata1[i, 1])  # molocular wight of any species
    xx.append(midata1[i, 2])  # molaur fraction of any species
    # gas canstant for any species per psia-ft.3/(lb-mole)-°R
    rgrg.append(midata1[i, 3])
    delhif.append(midata1[i, 4])  # Formation Enthalpy(ft^2/sec^2)
    # Vsa (Coffiecient of viscosity equestion for any species
    vsa.append(midata1[i, 5])
    # Vsb (Coffiecient of viscosity equestion for any species
    vsb.append(midata1[i, 6])
    # Vsc (Coffiecient of viscosity equestion for any species
    vsc.append(midata1[i, 7])


n_tab = midata2[1, 0]
tmptab, cptab01, cptab02, cptab03, cptab04, cptab05, cptab06 = [], [], [], [], [], [], []

for i in range(1, n_species+1):
    tmptab.append(midata2[i, 1])
    cptab01.append(midata2[i, 2])
    cptab02.append(midata2[i, 3])
    cptab03.append(midata2[i, 4])
    cptab04.append(midata2[i, 5])
    cptab05.append(midata2[i, 6])
    cptab06.append(midata2[i, 7])


ntab = midata3[1, 0]
htab01, htab02, htab03, htab04, htab05, htab06 = [], [], [], [], [], []

for i in range(1, n_species+1):
    tmptab.append(midata3[i, 1])
    htab01.append(midata3[i, 2])
    htab02.append(midata3[i, 3])
    htab03.append(midata3[i, 4])
    htab04.append(midata3[i, 5])
    htab05.append(midata3[i, 6])
    htab06.append(midata3[i, 7])


number = midata4[1, 0]
x_stem, tension_b = [], []

for i in range(1, number+1):
    x_stem.append(midata4[i, 1])
    tension_b.append(midata4[i, 2])


temp_amb = midata[1, 0]
press_amb = midata[1, 1]
depth = midata[1, 2]
pd = midata[1, 3]
st = tension_b[0]
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
rr = area_p / area_b
d_pipe = 5
d_av = np.sqrt(-tube_d**2 + casing_d**2)
teta *= 0.0174
map = 0
rg = 0


emi = np.zeros(n_species)

# Calculating constants
for i in range(n_species):
    map += map1[i] * xx[i]
    rg += rgrg[i] * xx[i]
    emi[i] = map1[i]


gama_gas = map / 29
tpc = 170.491 + 307.344 * gama_gas
ppc = 709.604 - 58.718 * gama_gas
row = 71
ro = 57.0
rol = wc * row + (1 - wc) * ro
g = 32.2
pd1 = pd
