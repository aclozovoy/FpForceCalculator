import math


def HfFunction(HfRadio, z, h, Ta):


    if HfRadio == 'PeriodKnown':
        z = float(z)
        h = float(h)
        Ta = float(Ta)

        a1 = min(1/Ta , 2.5)
        a2 = max(1 - (0.4 / Ta ) **2 , 0)
        Hf = 1 + a1 * (z/h) + a2 * (z/h)**10

        HfText = f"Hf = {Hf:.2f} (a1 = {a1:.2f}, a2 = {a2:.2f})"
        HfType ='Supported above grade by a building or nonbuilding structure with a known approximate fundamental period'

    elif HfRadio == 'PeriodUnknown':
        z = float(z)
        h = float(h)

        Hf = 1 + 2.5 * (z/h)
        a1 = None
        a2 = None

        HfText = f"Hf = {Hf:.2f}"
        HfType ='Supported above grade by a building or nonbuilding structure with an unknown approximate fundamental period'

    elif HfRadio == 'BelowGrade':
        Hf = 1.0
        a1 = None
        a2 = None

        HfText = "Hf = 1.00"
        HfType ='Supported at or below grade'

    return a1, a2, Hf, HfText, HfType


def RmuFunction(R, Omega0):

    R = float(R)
    Omega0 = float(Omega0)

    Rmu = (1.1 * R / Omega0)**(0.5)

    RmuText = f"R_mu = {Rmu:.2f}"

    return Rmu, RmuText



def IpFunction(IpRadio):

    if IpRadio == 'Ip1.0':
        Ip = 1.0
    elif IpRadio == 'Ip1.5':
        Ip = 1.5

    return Ip



def XFunction(Hf, Rmu, Car, Rpo):

    Car = float(Car)
    Rpo = float(Rpo)

    Xcalc = 0.4*(Hf/Rmu)*(Car/Rpo)

    if Xcalc > 1.6:
        X = 1.6
        XText = f"Fp = {X:.2f}*SdsIpWp (Fp was calculated as {Xcalc:.2f}*SdsIpWp, but is capped by the limit of 1.6 per XX.XX.XX)"
    elif Xcalc < 0.3:
        X = 0.3
        XText = f"Fp = {X:.2f}*SdsIpWp (Fp was calculated as {Xcalc:.2f}*SdsIpWp, but is capped by the limit of 0.3 per XX.XX.XX)"
    else:
        X = Xcalc
        XText = f"Fp = {X:.2f}*SdsIpWp"

    return X, Xcalc, XText


def FpFunction(X, Sds, Ip, Wp, Oop):

    Sds = float(Sds)
    Wp = float(Wp)
    Oop = float(Oop)

    Fp = X * Sds * Ip * Wp
    OopFp = Oop*Fp

    FpText = f"Fp = {Fp:.2f}"

    return Fp, FpText, OopFp