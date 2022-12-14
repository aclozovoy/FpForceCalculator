from flask import Blueprint, render_template, request
from functions import *

views = Blueprint('views', __name__)

@views.route('/', methods=['POST','GET'])
# @views.route('/main')
def main():
    if request.method == 'POST':

        # Sds Input
        Sds = request.form["Sds"]

        # Wp Input
        Wp = request.form["Wp"]

        # Units Input
        Units = request.form['Units']

        # Ip Input
        IpRadio = request.form['IpRadio']
        Ip = IpFunction(IpRadio)

        # Car Input
        Car = request.form["Car"]

        # Rpo Input
        Rpo = request.form["Rpo"]

        # Oop Input
        Oop = request.form["Oop"]

        # Hf Input and Calculation
        HfRadio = request.form['HfRadio']
        z = request.form['z']
        h = request.form['h']
        Ta = request.form['Ta']
        a1, a2, Hf, HfText = HfFunction(HfRadio, z, h, Ta)

        # R_mu Input and Calculation
        R = request.form['R']
        Omega0 = request.form['Omega0']
        Rmu, RmuText = RmuFunction(R, Omega0)

        # X Factor Calculation (X*SdsIpWp)
        X, Xcalc, XText = XFunction(Hf, Rmu, Car, Rpo)

        # Fp Calculation
        Fp, FpText, OopFp = FpFunction(X, Sds, Ip, Wp, Oop)


        return render_template('main.html', HfText=HfText, RmuText=RmuText, XText = XText, FpText=FpText)
    else:
        return render_template('main.html')







# @views.route("/about")
# def about():
#     return render_template("about.html")