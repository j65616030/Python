from flask import Flask, jsonify, request
from models import Libro
from database import db

app = Flask(__name__)

@app.route('/libros', methods=['GET'])
def get_libros():
    libros = Libro.query.all()
    return jsonify([libro.to_dict() for libro in libros])

@app.route('/libros', methods=['POST'])
def create_libro():
    data = request.get_json()
    libro = Libro(titulo=data['titulo'], autor=data['autor'])
    db.session.add(libro)
    db.session.commit()
    return jsonify(libro.to_dict())

@app.route('/libros/<int:id>', methods=['GET'])
def get_libro(id):
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({'error': 'Libro no encontrado'}), 404
    return jsonify(libro.to_dict())

@app.route('/libros/<int:id>', methods=['PUT'])
def update_libro(id):
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({'error': 'Libro no encontrado'}), 404
    data = request.get_json()
    libro.titulo = data['titulo']
    libro.autor = data['autor']
    db.session.commit()
    return jsonify(libro.to_dict())

@app.route('/libros/<int:id>', methods=['DELETE'])
def delete_libro(id):
    libro = Libro.query.get(id)
    if libro is None:
        return jsonify({'error': 'Libro no encontrado'}), 404
    db.session.delete(libro)
    db.session.commit()
    return jsonify({'message': 'Libro eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
