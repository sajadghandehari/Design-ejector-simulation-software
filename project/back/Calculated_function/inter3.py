def inter3(x, x1, x2, x3, f1, f2, f3):
    an1 = (x - x2) * (x - x3)
    an2 = (x - x1) * (x - x3)
    an3 = (x - x1) * (x - x2)
    dn1 = (x1 - x2) * (x1 - x3)
    dn2 = (x2 - x1) * (x2 - x3)
    dn3 = (x3 - x1) * (x3 - x2)
    cn1 = an1 / dn1
    cn2 = an2 / dn2
    cn3 = an3 / dn3
    f = cn1 * f1 + cn2 * f2 + cn3 * f3
    return f
