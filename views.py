from flask import Blueprint, render_template, request
from functions import *

views = Blueprint('views', __name__)

@views.route('/', methods=['POST','GET'])
# @views.route('/main')
def main():
    if request.method == 'POST':

        # Sds Input
        Sds = request.form["Sds"]

        # Hf Calculation
        HfRadio = request.form['HfRadio']
        z = request.form['z']
        h = request.form['h']
        Ta = request.form['Ta']
        a1, a2, Hf, HfText = HfFunction(HfRadio, z, h, Ta)

        return render_template('main.html', HfText=HfText)
    else:
        return render_template('main.html')







# @views.route("/about")
# def about():
#     return render_template("about.html")