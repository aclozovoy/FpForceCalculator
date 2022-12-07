import math


def HfFunction (HfRadio, z, h, Ta):


    if HfRadio == 'PeriodKnown':
        z = float(z)
        h = float(h)
        Ta = float(Ta)

        a1 = 1/Ta
        a2 = 1 - (0.4 / Ta ) **2
        Hf = 1 + a1 * (z/h) + a2 * (z/h)**10

        HfText = f"Hf = {Hf:.2f} (a1 = {a1:.2f}, a2 = {a2:.2f})"

    elif HfRadio == 'PeriodUnknown':
        z = float(z)
        h = float(h)

        Hf = 1 + 2.5 * (z/h)
        a1 = None
        a2 = None

        HfText = f"Hf = {Hf:.2f}"

    elif HfRadio == 'BelowGrade':
        Hf = 1.0
        a1 = None
        a2 = None

        HfText = "Hf = 1.00"

    return a1, a2, Hf, HfText

