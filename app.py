import json
import threading
from main import *
from flask import Flask
from flask import request, render_template, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/',methods=['GET'])
def inicio():    
    return render_template('init.html',nombrecito="Axel Garcia Tello & Elias Muñoz Primero")
    
@app.route('/calculate',methods=['POST'])
def calcular():    
    puntos.clear()
    arreglo = json.loads(request.form['arreglo'])
    if(len(arreglo)>0):
        puntos.clear()
    for tupla in arreglo:        
        puntos.append([int(tupla["x"]),int(tupla["y"])])
    print(puntos)
    respuesta = calcularDistanciasEuclidianas()
    hilo = threading.Thread(target=graficador)
    hilo.start()
    hilo.join()
    return jsonify(respuesta)

if __name__ == '__main__':    
    app.run(host='0.0.0.0',port=80,debug=True)