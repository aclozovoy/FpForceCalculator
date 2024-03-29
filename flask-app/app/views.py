from flask import Blueprint, render_template, request, Response
from .functions import *
from .db import *
import os

views = Blueprint('views', __name__)

@views.route('/', methods=['POST','GET'])
# @views.route('/main')
def main():
    if request.method == 'POST':

        # Sds Input
        Sds = request.form["Sds"]
        Sds = float(Sds)
        SdsT = f"{Sds:.3f}"

        # Wp Input
        Wp = request.form["Wp"]

        # Units Input
        units = request.form.get('units')

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
        Oop = float(Oop)
        OopT = f"{Oop:.2f}"

        # Component Number Input
        CompNum = request.form["CompNum"]
        CompTxt = CompFunction(CompNum)

        # Hf Input and Calculation
        HfRadio = request.form['HfRadio']
        z = request.form['z']
        h = request.form['h']
        Ta = request.form['Ta']
        a1, a2, Hf, HfText, HfType, CarType, HfCalc = HfFunction(HfRadio, z, h, Ta)
        HfT = f"{Hf:.2f}"

        # R_mu Input and Calculation
        R = request.form['R']
        R = float(R)
        Omega0 = request.form['Omega0']
        Omega0 = float(Omega0)
        Rmu, RmuText = RmuFunction(R, Omega0)
        RT = f"{R:.1f}"
        Omega0T = f"{Omega0:.2f}"
        RmuT = f"{Rmu:.2f}"

        # X Factor Calculation (X*SdsIpWp)
        X, Xcalc, XText = XFunction(Hf, Rmu, Car, Rpo)
        XT = f"{X:.2f}"
        XcalcT = f"{Xcalc:.2f}"

        # Fp Calculation
        Fp, FpText, OopFp = FpFunction(X, Sds, Ip, Wp, Oop)
        FpT = f"{Fp:.1f}"
        OopFpT = f"{OopFp:.1f}"

        # Text inputs for printout page
        info = [ request.form['title'], request.form['project'], request.form['location'], request.form['client'], request.form['company'], request.form['engineer'], request.form['date'], request.form['notes'] ]
        info_log = InfoFunction(info)

        # Log printout
        cursor = db_pages('printout')
        db_printout(cursor, Sds, Wp, units, R, Omega0, Rmu, z, h, Ta, Hf, Ip, Car, Rpo, Oop, CompNum, CompTxt, Fp, OopFp, info_log)

        return render_template('printout.html', HfText=HfText, RmuText=RmuText, CompTxt=CompTxt, HfCalc=HfCalc, XText = XText, OopFp=OopFpT, CarType=CarType, HfType=HfType, FpText=FpText, Omega0=Omega0T, Oop=OopT, R=RT, Sds=SdsT, Hf=HfT, Rmu=RmuT, Car=CarT, Rpo=RpoT, X=XT, Xcalc=XcalcT, Fp=FpT, Wp=Wp, units=units, Ip=Ip, info=info)
    else:

        # Log main page visits 
        cursor = db_pages('main')
        
        return render_template('main.html')



# About page
@views.route("/about")
def about():
    db_pages('about')
    return render_template("about.html")

# Feedback page
@views.route("/feedback", methods=['POST','GET'])
def feedback():
    if request.method == 'POST':

        # Feedback Input
        feedback = request.form['feedback']
        feedback_single = " (N) ".join(line.strip() for line in feedback.splitlines())

        # Log feedback
        cursor = db_pages('thankyou')
        db_feedback(cursor, feedback_single)

        return render_template('thankyou.html')

    else:

        # Log feedback page visits
        cursor = db_pages('feedback')

        return render_template("feedback.html")
    
# Health
@views.route("/health")
def health():
    return Response("OK", status=200)


# Env Var Check
@views.route("/env")
def env():

    try:
        env = os.environ['DB_PASSWORD']
    except:
        env = "No environment variable"

    return Response(env, status=200)