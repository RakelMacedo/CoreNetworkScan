from flask import Flask, jsonify, redirect, url_for
from pymongo import MongoClient
from scanners import TCP, Ethernet

# Configuração do MongoDB
client = MongoClient('mongodb://localhost:27017/') 
db = client['CoreNetwork']  

app = Flask(__name__)


@app.route('/')
def hello_world():
    with open('index.html', 'r') as file:
        content = file.read()
    return content


@app.route('/tcp/start', methods=['GET'])
def TCP_start():
    
    TCP()

    # Redireciona para a rota /tcp /data
    return redirect(url_for('TCP_data'))


@app.route('/tcp/data', methods=['GET'])
def TCP_data():
    # Consulta os dados no MongoDB e os retorna em JSON
    TCP_data = list(db.TCP.find({}, {"_id": 0}))
    return jsonify(TCP_data), 200


@app.route('/ethernet/start', methods=['GET'])
def Ethernet_start():
    Ethernet()
    # Redireciona para a rota /tcp /data
    return redirect(url_for('Ethernet_data'))


@app.route('/ethernet/data', methods=['GET'])
def Ethernet_data():
    # Consulta os dados no MongoDB e os retorna em JSON
    Ethernet_data = list(db.ETHERNET.find({}, {"_id": 0}))
    return jsonify(Ethernet_data), 200


if __name__ == '__main__':
    app.run(debug=True) 

