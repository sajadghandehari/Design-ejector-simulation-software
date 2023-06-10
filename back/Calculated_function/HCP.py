import numpy as np
from input_data import *
from Calculated_function.inter3 import *


def HCP(tr):
    smalt = 0.000001
    fac = 1 + smalt
    jc = 0
    jc = jc + 1
    while jc <= ntab:
        if tr > tmptab[jc] * fac:
            jc = jc + 1
            if jc > ntab:
                break
        else:
            break
    if jc < 2:
        jc = 2
    if jc > ntab - 1:
        jc = ntab - 1

    hifac1 = [0] * 6
    h1ii = [0] * 6
    cp1ii = [0] * 6

    hifac1[0] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], htab01[jc-1], htab01[jc], htab01[jc+1])
    h1ii[0] = hifac1[0] * tr + delhif[0]

    hifac1[1] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], htab02[jc-1], htab02[jc], htab02[jc+1])
    h1ii[1] = hifac1[1] * tr + delhif[1]

    hifac1[2] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], htab03[jc-1], htab03[jc], htab03[jc+1])
    h1ii[2] = hifac1[2] * tr + delhif[2]

    hifac1[3]= inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], htab04[jc-1], htab04[jc], htab04[jc+1])
    h1ii[3] = hifac1[3] * tr + delhif[3]

    hifac1[4] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], htab05[jc-1], htab05[jc], htab05[jc+1])
    h1ii[4] = hifac1[4] * tr + delhif[4]

    hifac1[5] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], htab06[jc-1], htab06[jc], htab06[jc+1])
    h1ii[5] = hifac1[5] * tr + delhif[5]


    cp1ii[0] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], cptab01[jc-1], cptab01[jc], cptab01[jc+1])
    cp1ii[1] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], cptab02[jc-1], cptab02[jc], cptab02[jc+1])
    cp1ii[2] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], cptab03[jc-1], cptab03[jc], cptab03[jc+1])
    cp1ii[3] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], cptab04[jc-1], cptab04[jc], cptab04[jc+1])
    cp1ii[4] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], cptab05[jc-1], cptab05[jc], cptab05[jc+1])
    cp1ii[5] = inter3(tr, tmptab[jc-1], tmptab[jc], tmptab[jc+1], cptab06[jc-1], cptab06[jc], cptab06[jc+1])



    if ns == 6:
        cpii = [cp1ii[0], cp1ii[1], cp1ii[2], cp1ii[3], cp1ii[4], cp1ii[5]]
        hifac = [hifac1[0], hifac1[1], hifac1[2], hifac1[3], hifac1[4], hifac1[5]]
        hii = [h1ii[0], h1ii[1], h1ii[2], h1ii[3], h1ii[4], h1ii[5]]
    if ns == 2:
        cpii = [cp1ii[0], cp1ii[1]]
        hifac = [hifac1[0], hifac1[1]]
        hii = [h1ii[0], h1ii[1]]

    return cpii, hifac, hii
