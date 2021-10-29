from main import *
from flask import Flask
from flask import request, render_template, url_for, redirect, flash, session, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/',methods=['GET'])
def inicio():
    return render_template('init.html',nombrecito="Métodos")
    # calcularDistanciasEuclidianas()
    # return "Hi"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)