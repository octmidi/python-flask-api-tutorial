from flask import Flask
from flask import Flask, jsonify
from flask import request
import json


app = Flask(__name__)
@app.route('/todos', methods=['GET'])
# http://localhost:3245/todos
def read_json():
    
     with open("sample.json", 'r', encoding='utf-8') as infile:
        data = json.load(infile)
     return jsonify(data)


def agregar_elemento(nuevo_elemento):
    # Intenta leer el contenido actual del archivo JSON
    try:
        with open("sample.json", 'r', encoding='utf-8') as infile:
            data = json.load(infile)
    except FileNotFoundError:
        # Si el archivo no existe, inicializa la lista vacía
        data = []

    # Agrega el nuevo elemento a la lista
    data.append(nuevo_elemento)

    # Serializa la lista de datos a formato JSON
    json_object = json.dumps(data, indent=4,ensure_ascii=False)

    # Escribe la lista de datos de vuelta al archivo JSON
    with open("sample.json", 'w', encoding='utf-8') as outfile:
        outfile.write(json_object)

# Nuevo elemento que deseas agregar


        
    
@app.route('/todos', methods=['POST'])
# http://localhost:3245/todos

def add_new_todo():
    new_todo = {
    "Name": "Demian", 
    "Last_Name": "Hermann Hesse",
    "Age":"74",
    "Address":"Born 156"
    }

    agregar_elemento(new_todo)
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'



@app.route('/todos/<int:position>', methods=['DELETE'])
# http://localhost:3245/todos/1 

def delete_todo(position):
    # Lee el contenido actual del archivo JSON
    with open("sample.json", 'r') as infile:
        data = json.load(infile)

    # Verifica si la posición proporcionada es válida
    if 0 <= position < len(data):
        # Elimina el elemento en la posición dada
        deleted_todo = data.pop(position)

        # Escribe el objeto actualizado de vuelta al archivo JSON
        with open("sample.json", 'w') as outfile:
            json.dump(data, outfile, indent=2)

        print(f'Deleted todo at position {position}: {deleted_todo}')
        return f'Deleted todo at position {position}: {deleted_todo}'
    else:
        return 'Invalid position'
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

