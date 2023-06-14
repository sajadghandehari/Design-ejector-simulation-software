import numpy as np
# from input_data import *
from back.Calculated_function.inter3 import *


def HCP(self, tr):
    smalt = 0.000001
    fac = 1 + smalt
    jc = 0
    jc = jc + 1
    while jc <= self.ntab:
        if tr > self.tmptab[jc] * fac:
            jc = jc + 1
            if jc > self.ntab:
                break
        else:
            break
    if jc < 2:
        jc = 2
    if jc > self.ntab - 1:
        jc = self.ntab - 1

    hifac1 = [0] * 6
    h1ii = [0] * 6
    cp1ii = [0] * 6

    hifac1[0] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.htab01[jc-1], self.htab01[jc], self.htab01[jc+1])
    h1ii[0] = hifac1[0] * tr + self.delhif[0]

    hifac1[1] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.htab02[jc-1], self.htab02[jc], self.htab02[jc+1])
    h1ii[1] = hifac1[1] * tr + self.delhif[1]

    hifac1[2] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.htab03[jc-1], self.htab03[jc], self.htab03[jc+1])
    h1ii[2] = hifac1[2] * tr + self.delhif[2]

    hifac1[3]= inter3(tr, self.tmptab[jc-1], self.tmptab[jc],self. tmptab[jc+1], self.htab04[jc-1], self.htab04[jc], self.htab04[jc+1])
    h1ii[3] = hifac1[3] * tr + self.delhif[3]

    hifac1[4] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.htab05[jc-1], self.htab05[jc], self.htab05[jc+1])
    h1ii[4] = hifac1[4] * tr + self.delhif[4]

    hifac1[5] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.htab06[jc-1], self.htab06[jc], self.htab06[jc+1])
    h1ii[5] = hifac1[5] * tr + self.delhif[5]


    cp1ii[0] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.cptab01[jc-1], self.cptab01[jc], self.cptab01[jc+1])
    cp1ii[1] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.cptab02[jc-1], self.cptab02[jc], self.cptab02[jc+1])
    cp1ii[2] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.cptab03[jc-1], self.cptab03[jc], self.cptab03[jc+1])
    cp1ii[3] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.cptab04[jc-1], self.cptab04[jc], self.cptab04[jc+1])
    cp1ii[4] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.cptab05[jc-1], self.cptab05[jc], self.cptab05[jc+1])
    cp1ii[5] = inter3(tr, self.tmptab[jc-1], self.tmptab[jc], self.tmptab[jc+1], self.cptab06[jc-1], self.cptab06[jc], self.cptab06[jc+1])



    if self.ns == 6:
        cpii = [cp1ii[0], cp1ii[1], cp1ii[2], cp1ii[3], cp1ii[4], cp1ii[5]]
        hifac = [hifac1[0], hifac1[1], hifac1[2], hifac1[3], hifac1[4], hifac1[5]]
        hii = [h1ii[0], h1ii[1], h1ii[2], h1ii[3], h1ii[4], h1ii[5]]
    if self.ns == 2:
        cpii = [cp1ii[0], cp1ii[1]]
        hifac = [hifac1[0], hifac1[1]]
        hii = [h1ii[0], h1ii[1]]

    return cpii, hifac, hii
