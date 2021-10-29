import json
from main import *
from flask import Flask
from flask import request, render_template, url_for, redirect, flash, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')
coordenadas = list()

@app.route('/',methods=['GET'])
def inicio():
    return render_template('init.html',nombrecito="Axel Garcia Tello & Elias Muñoz Primero")
    
@app.route('/calculate',methods=['POST'])
def calcular():    
    arreglo = json.loads(request.form['arreglo'])
    if(len(arreglo)>0):
        puntos.clear()
    for tupla in arreglo:        
        puntos.append([int(tupla["x"]),int(tupla["y"])])
    print(puntos)
    respuesta = calcularDistanciasEuclidianas()
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)