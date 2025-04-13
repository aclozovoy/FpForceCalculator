from flask import Blueprint, render_template, request, jsonify
from .functions import *
from datetime import datetime

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

@views.route('/printout', methods=['GET'])
def printout():
    try:
        # Get the calculation data from the session or request
        data = request.args
        
        # Extract and validate input data
        Sds = float(data.get('Sds', 0))
        Wp = float(data.get('Wp', 0))
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

        # Default project info
        info = [
            "Nonstructural Seismic Force Calculation",
            "Project Name",
            "Location",
            "Client Name",
            "Company Name",
            "Engineer Name",
            datetime.now().strftime("%m/%d/%Y"),
            "Notes: This calculation is based on ASCE 7-22, Chapter 13."
        ]

        return render_template('printout.html',
                             info=info,
                             Sds=Sds,
                             Wp=Wp,
                             Ip=Ip,
                             Car=Car,
                             Rpo=Rpo,
                             Oop=Oop,
                             CompTxt=CompTxt,
                             CarType=CarType,
                             R=R,
                             Omega0=Omega0,
                             Rmu=Rmu,
                             RmuText=RmuText,
                             Hf=Hf,
                             HfText=HfText,
                             HfType=HfType,
                             HfCalc=HfCalc,
                             X=X,
                             Xcalc=Xcalc,
                             XText=XText,
                             Fp=Fp,
                             FpText=FpText,
                             OopFp=OopFp)
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@views.route('/get_component_params', methods=['POST'])
def get_component_params():
    try:
        data = request.get_json()
        component_name = data.get('component_name')
        support_condition = data.get('support_condition', 'above')  # Default to 'above'
        
        if not component_name:
            return jsonify({'success': False, 'error': 'Component name is required'}), 400
            
        params = getArchitecturalComponentParams(component_name)
        
        # Select the appropriate Car value based on support condition
        if support_condition == 'below':
            params['Car'] = params['Car_below']
        else:
            params['Car'] = params['Car_above']
            
        # Remove the separate Car values since we've selected the appropriate one
        del params['Car_above']
        del params['Car_below']
        
        return jsonify({
            'success': True,
            'params': params
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400