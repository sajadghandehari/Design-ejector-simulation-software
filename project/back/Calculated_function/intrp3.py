from .inter3 import *

def intrp3(xxx, x1, y1, npnts):
    smalt = 0.000001
    fac = 1 + smalt
    for jc in range(1, npnts + 1):
        if xxx <= (x1[jc-1] * fac):
            break
    if jc < 2:
        jc = 2
    if jc > (npnts - 1):
        jc = npnts - 1
    yy2 = inter3(xxx, x1[jc-2], x1[jc-1], x1[jc], y1[jc-2], y1[jc-1], y1[jc])
    yy1 = yy2
    return yy1


