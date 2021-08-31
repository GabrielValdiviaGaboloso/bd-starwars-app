from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate
from models import db, Planeta, Personajes, Usuario, Favoritos

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
Migrate(app, db)


@app.route('/')
def main():
    return render_template('index.html')


# @app.route('/people', methods=['GET'])
# def get_all_people():
#     personajes = Personajes.query.all()
#     personajes = list(
#         map(lambda personajes: personajes.serialize(), personajes))
#     return jsonify(personajes), 200


# @app.route('/people', methods=['POST'])
# def Post_crear_all_people():
#     nombre = request.json.get('nombre')
#     altura = request.json.get('altura')
#     masa = request.json.get('masa')
#     color_cabello = request.json.get('color_cabello')
#     color_piel = request.json.get('color_piel')
#     color_ojos = request.json.get('color_ojos')
#     fecha_nacimiento = request.json.get('fecha_nacimiento')
#     genero = request.json.get(' genero')
#     creacion = request.json.get('creacion')
#     editado = request.json.get('editado')

#     personajes = Personajes()
#     personajes.nombre = nombre
#     personajes.altura = altura
#     personajes.masa = masa
#     personajes.color_cabello = color_cabello
#     personajes.color_piel = color_piel
#     personajes.color_ojos = color_ojos
#     personajes.fecha_nacimiento = fecha_nacimiento
#     personajes.genero = genero
#     personajes.creacion = creacion
#     personajes.editado = editado

#     db.session.add(personajes)
#     db.session.commit()

#     return jsonify(personajes.serialize()), 201


# @app.route('/people/<int:id>', methods=['PUT'])
# def update_personajes(id):
#     nombre = request.json.get('nombre')
#     altura = request.json.get('altura')
#     masa = request.json.get('masa')
#     color_cabello = request.json.get('color_cabello')
#     color_piel = request.json.get('color_piel')
#     color_ojos = request.json.get('color_ojos')
#     fecha_nacimiento = request.json.get('fecha_nacimiento')
#     genero = request.json.get(' genero')
#     creacion = request.json.get('creacion')
#     editado = request.json.get('editado')

#     personajes = Personajes.query.get(id)

#     personajes.nombre = nombre
#     personajes.altura = altura
#     personajes.masa = masa
#     personajes.color_cabello = color_cabello
#     personajes.color_piel = color_piel
#     personajes.color_ojos = color_ojos
#     personajes.fecha_nacimiento = fecha_nacimiento
#     personajes.genero = genero
#     personajes.creacion = creacion
#     personajes.editado = editado

#     db.session.commit()

#     return jsonify(personajes.serialize()), 200


# @app.route('/people/<int:id>', methods=['DELETE'])
# def Delete_personajes(id):

#     personajes = Personajes.query.get(id)
#     db.session.delete(personajes)
#     db.session.commit()

#     return jsonify({"success": "Personajes delete"}), 200


@app.route('/people', methods=['GET', 'POST'])
@app.route('/people/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def Personajes_all(id=None):
    if request.method == 'GET':

        if id is not None:
            personajes = Personajes.query.get(id)
            return jsonify(personajes.serialize()), 200

        personajes = Personajes.query.all()
        personajes = list(
            map(lambda personajes: personajes.serialize(), personajes))
        return jsonify(personajes), 200

    if request.method == 'POST':
        nombre = request.json.get('nombre')
        altura = request.json.get('altura')
        masa = request.json.get('masa')
        color_cabello = request.json.get('color_cabello')
        color_piel = request.json.get('color_piel')
        color_ojos = request.json.get('color_ojos')
        fecha_nacimiento = request.json.get('fecha_nacimiento')
        genero = request.json.get('genero')
        creacion = request.json.get('creacion')
        editado = request.json.get('editado')

        personajes = Personajes()
        personajes.nombre = nombre
        personajes.altura = altura
        personajes.masa = masa
        personajes.color_cabello = color_cabello
        personajes.color_piel = color_piel
        personajes.color_ojos = color_ojos
        personajes.fecha_nacimiento = fecha_nacimiento
        personajes.genero = genero
        personajes.creacion = creacion
        personajes.editado = editado

        # db.session.add(personajes)
        # db.session.commit()
        personajes.save()

        return jsonify(personajes.serialize()), 201

    if request.method == 'PUT':
        nombre = request.json.get('nombre')
        altura = request.json.get('altura')
        masa = request.json.get('masa')
        color_cabello = request.json.get('color_cabello')
        color_piel = request.json.get('color_piel')
        color_ojos = request.json.get('color_ojos')
        fecha_nacimiento = request.json.get('fecha_nacimiento')
        genero = request.json.get('genero')
        creacion = request.json.get('creacion')
        editado = request.json.get('editado')

        personajes = Personajes.query.get(id)

        personajes.nombre = nombre
        personajes.altura = altura
        personajes.masa = masa
        personajes.color_cabello = color_cabello
        personajes.color_piel = color_piel
        personajes.color_ojos = color_ojos
        personajes.fecha_nacimiento = fecha_nacimiento
        personajes.genero = genero
        personajes.creacion = creacion
        personajes.editado = editado

        # db.session.commit()
        personajes.update()

        return jsonify(personajes.serialize()), 200

    if request.method == 'DELETE':
        personajes = Personajes.query.get(id)

        # db.session.delete(personajes)
        # db.session.commit()
        personajes.delete()

        return jsonify({"success": "Personajes delete"}), 200

# # --------------------------------------------------------------------------------


@app.route('/planeta', methods=['GET', 'POST'])
@app.route('/planeta/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def Planeta_all(id=None):
    if request.method == 'GET':
        if id is not None:
            planeta = Planeta.query.get(id)
            return jsonify(planeta.serialize()), 200
        planeta = Planeta.query.all()
        planeta = list(map(lambda planeta: planeta.serialize(), planeta))
        return jsonify(planeta), 200

    if request.method == 'POST':
        diametro = request.json.get('diametro')
        periodo_rotacion = request.json.get('periodo_rotacion')
        periodo_orbital = request.json.get('periodo_orbital')
        gravedad = request.json.get('gravedad')
        poblacion = request.json.get('poblacion')
        clima = request.json.get('clima')
        terreno = request.json.get('terreno')
        superfice_acuatica = request.json.get('superfice_acuatica')
        creacion = request.json.get('creacion')
        editado = request.json.get('editado')
        nombre = request.json.get('nombre')

        planeta = Planeta()

        planeta.diametro = diametro
        planeta.periodo_rotacion = periodo_rotacion
        planeta.diametperiodo_orbitalro = periodo_orbital
        planeta.gravedad = gravedad
        planeta.poblacion = poblacion
        planeta.clima = clima
        planeta.terreno = terreno
        planeta.superfice_acuatica = superfice_acuatica
        planeta.creacion = creacion
        planeta.editado = editado
        planeta.nombre = nombre

        # db.session.add(planeta)
        # db.session.commit()
        planeta.save()

        return jsonify(planeta.serialize()), 201

    if request.method == 'PUT':
        diametro = request.json.get('diametro')
        periodo_rotacion = request.json.get('periodo_rotacion')
        periodo_orbital = request.json.get('periodo_orbital')
        gravedad = request.json.get('gravedad')
        poblacion = request.json.get('poblacion')
        clima = request.json.get('clima')
        terreno = request.json.get('terreno')
        superfice_acuatica = request.json.get('superfice_acuatica')
        creacion = request.json.get('creacion')
        editado = request.json.get('editado')
        nombre = request.json.get('nombre')

        planeta = Planeta.query.get(id)

        planeta.diametro = diametro
        planeta.periodo_rotacion = periodo_rotacion
        planeta.diametperiodo_orbitalro = periodo_orbital
        planeta.gravedad = gravedad
        planeta.poblacion = poblacion
        planeta.clima = clima
        planeta.terreno = terreno
        planeta.superfice_acuatica = superfice_acuatica
        planeta.creacion = creacion
        planeta.editado = editado
        planeta.nombre = nombre

        # db.session.commit()
        planeta.update()

        return jsonify(planeta.serialize()), 200

    if request.method == 'DELETE':
        planeta = Planeta.query.get(id)
        # db.session.delete(planeta)
        # db.session.commit()
        planeta.delete()

        return jsonify({"success": "Planeta delete"}), 200

# # --------------------------------------------------------------------------------


@app.route('/usuario', methods=['GET', 'POST'])
def List_usuario():
    if request.method == 'GET':

        usuario = Usuario.query.all()
        usuario = list(map(lambda usuario: usuario.serialize(), usuario))
        return jsonify(usuario), 200

    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('password')

        usuario = Usuario()

        usuario.email = email
        usuario.password = password

        # db.session.add(usuario)
        # db.session.commit()
        usuario.save()

        return jsonify(usuario.serialize()), 201

# # --------------------------------------------------------------------------------


@app.route('/usuario/<int:id>', methods=['GET', 'POST'])
def lista_favorito(id):
    usuario = Usuario.query.get(id)
    return jsonify(usuario.serialize()), 200


if __name__ == '__main__':
    app.run()
