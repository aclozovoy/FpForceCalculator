from flask import Blueprint, render_template, request
from functions import *

views = Blueprint("views", __name__)

@views.route("/", methods=["POST","GET"])
# @views.route("/main")
def main():
    if request.method == "POST":

        # Sds Input
        # Sds = float(request.form["Sds"])

        # Hf Calculation
        
        z = float(request.form["z"])
        h = float(request.form["h"])
        Ta = float(request.form["Ta"])
        a1, a2, Hf = heightfactor(z, h, Ta)

        return render_template('main.html', a1=str(a1), a2=str(a2), Hf=str(Hf))
    else:
        return render_template('main.html')







# @views.route("/about")
# def about():
#     return render_template("about.html")