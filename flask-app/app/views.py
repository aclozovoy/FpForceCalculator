from flask import Blueprint, render_template, request, jsonify
from .functions import *

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def main():
    return render_template('main.html')

@views.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        # Extract and validate input data
        Sds = float(data.get('Sds', 0))
        Wp = float(data.get('Wp', 0))
        units = data.get('units', 'metric')
        Ip = IpFunction(data.get('IpRadio', '1'))
        Car = float(data.get('Car', 0))
        Rpo = float(data.get('Rpo', 0))
        Oop = float(data.get('Oop', 0))
        CompNum = data.get('CompNum', '1')
        CompTxt = CompFunction(CompNum)
        
        # Calculate Hf
        HfRadio = data.get('HfRadio', '1')
        z = float(data.get('z', 0))
        h = float(data.get('h', 0))
        Ta = float(data.get('Ta', 0))
        a1, a2, Hf, HfText, HfType, CarType, HfCalc = HfFunction(HfRadio, z, h, Ta)
        
        # Calculate R_mu
        R = float(data.get('R', 0))
        Omega0 = float(data.get('Omega0', 0))
        Rmu, RmuText = RmuFunction(R, Omega0)
        
        # Calculate X Factor
        X, Xcalc, XText = XFunction(Hf, Rmu, Car, Rpo)
        
        # Calculate Fp
        Fp, FpText, OopFp = FpFunction(X, Sds, Ip, Wp, Oop)
        
        return jsonify({
            'success': True,
            'results': {
                'Hf': round(Hf, 2),
                'HfText': HfText,
                'Rmu': round(Rmu, 2),
                'RmuText': RmuText,
                'CompTxt': CompTxt,
                'HfCalc': HfCalc,
                'XText': XText,
                'OopFp': round(OopFp, 1),
                'CarType': CarType,
                'HfType': HfType,
                'FpText': FpText,
                'Fp': round(Fp, 1),
                'X': round(X, 2),
                'Xcalc': round(Xcalc, 2)
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200