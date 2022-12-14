from flask import Blueprint, render_template, request
from functions import *

views = Blueprint('views', __name__)

@views.route('/', methods=['POST','GET'])
# @views.route('/main')
def main():
    if request.method == 'POST':

        # Sds Input
        Sds = request.form["Sds"]
        Sds = float(Sds)
        SdsT = f"{Sds:.3f}"
        # SdsT = str(round(Sds, 3))

        # Wp Input
        Wp = request.form["Wp"]

        # Units Input
        Units = request.form.get('Units')

        # Ip Input
        IpRadio = request.form['IpRadio']
        Ip = IpFunction(IpRadio)

        # Car Input
        Car = request.form["Car"]
        Car = float(Car)
        CarT = f"{Car:.2f}"

        # Rpo Input
        Rpo = request.form["Rpo"]
        Rpo = float(Rpo)
        RpoT = f"{Rpo:.2f}"

        # Oop Input
        Oop = request.form["Oop"]

        # Component Number Input
        CompNum = request.form.get("CompNum")

        # Hf Input and Calculation
        HfRadio = request.form['HfRadio']
        z = request.form['z']
        h = request.form['h']
        Ta = request.form['Ta']
        a1, a2, Hf, HfText = HfFunction(HfRadio, z, h, Ta)
        HfT = f"{Hf:.2f}"

        # R_mu Input and Calculation
        R = request.form['R']
        Omega0 = request.form['Omega0']
        Rmu, RmuText = RmuFunction(R, Omega0)
        RmuT = f"{Rmu:.2f}"

        # X Factor Calculation (X*SdsIpWp)
        X, Xcalc, XText = XFunction(Hf, Rmu, Car, Rpo)
        XT = f"{X:.2f}"
        XcalcT = f"{Xcalc:.2f}"

        # Fp Calculation
        Fp, FpText, OopFp = FpFunction(X, Sds, Ip, Wp, Oop)
        FpT = f"{Fp:.2f}"

        # List = [Sds, Wp, Units, Ip, Car, Rpo, Oop, CompNum, HfRadio, z, h, Ta, a1, a2]

        return render_template('printout.html', HfText=HfText, RmuText=RmuText, XText = XText, FpText=FpText, Sds=SdsT, Hf=HfT, Rmu=RmuT, Car=CarT, Rpo=RpoT, X=XT, Xcalc=XcalcT, Fp=FpT ,Wp=Wp, Units=Units, CompNum=CompNum, Ip=Ip)
    else:
        return render_template('main.html')







# @views.route("/about")
# def about():
#     return render_template("about.html")