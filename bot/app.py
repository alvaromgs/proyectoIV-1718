from listas import *
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(status='OK')

@app.route('/listas')
def listas():
    return jsonify(getLists())

@app.route('/lista')
def lista():
    if 'id' in request.args:
        if request.args['id'] in pelis:
            return jsonify(getList(request.args['id']))
        else:
            return "No se ha encontrado una lista con el id indicado"
    else:
        return "Indica la lista que quieras consultar a través del parámetro GET 'id'. Ejemplo: /lista?id=Favoritas"

@app.route('/add')
def add():
    if all (arg in request.args for arg in ('title', 'rating', 'id')):
        if request.args['id'] in pelis:
            updateMovie(request.args['id'], request.args['title'], float(request.args['rating']))
            return jsonify(getList(request.args['id']))
        else:
            return "No se ha encontrado una lista con el id indicado"
    else:
        return "Indica la película, puntuación y la lista a la que quieras añadirla a través de los parámetros GET 'title', 'rating' y 'id' respectivamente. Ejemplo: /add?title=Gladiator&rating=8.5&id=Favoritas"

if __name__ == '__main__':
    app.run()