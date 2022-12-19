import math


def HfFunction(HfRadio, z, h, Ta):


    if HfRadio == 'PeriodKnown':
        z = float(z)
        h = float(h)
        Ta = float(Ta)

        a1 = min(1/Ta , 2.5)
        a1calc = 1/Ta
        a2 = max(1 - (0.4 / Ta ) **2 , 0)
        a2calc = 1 - (0.4 / Ta ) **2
        Hf = 1 + a1 * (z/h) + a2 * (z/h)**10

        HfText = f"Hf = {Hf:.2f} (a1 = {a1:.2f}, a2 = {a2:.2f})"
        HfType ='Supported above grade by a building or nonbuilding structure with a known approximate fundamental period'
        CarType = '(Supported above grade by a structure)'

        HfCalc = f'''
        <p>z = {z:.0f} ft</p>
        <p>h = {h:.0f} ft</p>
        <p>T<sub>a</sub> = {Ta:.2f}</p>
        <p>H<sub>f</sub> = 1 + a<sub>1</sub>(z/h) + a<sub>2</sub>(z/h)<sup>10</sup></p>
        <p>&emsp;a<sub>1</sub> = min(1/T<sub>a</sub> , 2.5) = min(1/{Ta:.2f} , 2.5) = min({a1calc:.2f} , 2.5) = {a1:.2f}</p>
        <p>&emsp;a<sub>2</sub> = max(1 - (0.4/T<sub>a</sub>)<sup>2</sup> , 0) = max(1 - (0.4/{Ta:.2f})<sup>2</sup> , 0) = max({a2calc:.2f} , 0) = {a2:.2f}</p>
        <p>H<sub>f</sub> = 1 + {a1:.2f}( {z:.0f}ft / {h:.0f}ft ) + {a2:.2f}( {z:.0f}ft / {h:.0f}ft )<sup>10</sup></p>
        <p>H<sub>f</sub> = {Hf:.2f}</p>
        '''



    elif HfRadio == 'PeriodUnknown':
        z = float(z)
        h = float(h)

        Hf = 1 + 2.5 * (z/h)
        a1 = None
        a2 = None

        HfText = f"Hf = {Hf:.2f}"
        HfType ='Supported above grade by a building or nonbuilding structure with an unknown approximate fundamental period'
        CarType = '(Supported above grade by a structure)'

        HfCalc = f'''
        <p>z = {z:.0f} ft</p>
        <p>h = {h:.0f} ft</p>
        <p>H<sub>f</sub> = 1 + 2.5(z/h)</p>
        <p>H<sub>f</sub> = 1 + 2.5({z:.0f}ft /{h:.0f}ft )</p>
        <p>H<sub>f</sub> = {Hf:.2f}</p>
        '''

    elif HfRadio == 'BelowGrade':
        Hf = 1.0
        a1 = None
        a2 = None

        HfText = "Hf = 1.00"
        HfType ='Supported at or below grade'
        CarType ='(Supported at or below grade)'

        HfCalc = f'''
        <p>H<sub>f</sub> = {Hf:.2f}</p>
        '''

    return a1, a2, Hf, HfText, HfType, CarType, HfCalc


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

def CompFunction(CompNum):

    i = int(CompNum) - 1
    CompList = (
        'Interior nonstructural walls and partitions: Light frame ≤ 9ft (2.74m) in height',
        'Interior nonstructural walls and partitions: Light frame > 9ft (2.74m) in height',
        'Interior nonstructural walls and partitions: Reinforced Masonry',
        'Interior nonstructural walls and partitions: All other walls and partitions',
        'Cantilever elements (unbraced or braced to structure below its center of mass): Parapets and cantilever interior nonstructural walls',
        'Cantilever elements (unbraced or braced to structure below its center of mass): Chimneys where laterally braced or supported by the structural frame',
        'Cantilever elements (braced to structural frame above its center of mass): Parapets',
        'Cantilever elements (braced to structural frame above its center of mass): Chimneys',
        'Cantilever elements (braced to structural frame above its center of mass): Exterior nonstructural walls',
        'Exterior nonstructural wall elements and connections: Wall element',
        'Exterior nonstructural wall elements and connections: Body of wall panel connections',
        'Exterior nonstructural wall elements and connections: Fasteners of the connecting system',
        'Veneer: Limited deformability elements and attachments',
        'Veneer: Low deformability elements and attachments',
        'Penthouses (except where framed by an extension of the building frame): Seismic Force-Resisting Systems with R≥6',
        'Penthouses (except where framed by an extension of the building frame): Seismic Force-Resisting Systems with 6>R≥4',
        'Penthouses (except where framed by an extension of the building frame): Seismic Force-Resisting Systems with R<4',
        'Penthouses (except where framed by an extension of the building frame): Other Systems',
        'Ceilings: All',
        'Cabinets: Permanent floor-supported storage cabinets more than 6 ft (1,829 mm) tall, including contents',
        'Cabinets: Permanent floor-supported library shelving, book stacks, and bookshelves more than 6 ft (1,829 mm) tall, including contents',
        'Laboratory equipment',
        'Access Floors: Special access floors (designed in accordance with Section 13.5.7.2)',
        'Access Floors: All other',
        'Appendages and ornamentations',
        'Signs and Billboards',
        'Other rigid components',
        'Other flexible components: High-deformability elements and attachments',
        'Other flexible components: Limited-deformability elements and attachments',
        'Other flexible components: Low-deformability elements and attachments',
        'Egress stairways not part of the building seismic force-resisting system',
        'Egress stairs and ramp fasteners and attachments'
    )

    CompTxt = CompList[i]

    return CompTxt