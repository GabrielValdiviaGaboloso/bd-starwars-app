from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
db = SQLAlchemy()


class Personajes(db.Model):
    __tablename__ = 'Personajes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    altura = db.Column(db.String(250))
    masa = db.Column(db.String(250))
    color_cabello = db.Column(db.String(250))
    color_piel = db.Column(db.String(250))
    color_ojos = db.Column(db.String(250))
    fecha_nacimiento = db.Column(db.String(250))
    genero = db.Column(db.String(250))
    creacion = db.Column(db.String(250))
    editado = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "altura": self.altura,
            "masa": self.masa,
            "color_cabello": self.color_cabello,
            "color_piel": self.color_piel,
            "color_ojos": self.color_ojos,
            "fecha_nacimiento": self.fecha_nacimiento,
            "genero": self.genero,
            "creacion": self.creacion,
            "editado": self.editado
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Planeta(db.Model):
    __tablename__ = 'Planeta'
    id = db.Column(db.Integer, primary_key=True)
    diametro = db.Column(db.String(250))
    periodo_rotacion = db.Column(db.String(250))
    periodo_orbital = db.Column(db.String(250))
    gravedad = db.Column(db.String(250))
    poblacion = db.Column(db.String(250))
    clima = db.Column(db.String(250))
    terreno = db.Column(db.String(250))
    superfice_acuatica = db.Column(db.String(250))
    creacion = db.Column(db.String(250))
    editado = db.Column(db.String(250))
    nombre = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
            "diametro": self.diametro,
            "periodo_rotacion": self.periodo_rotacion,
            "periodo_orbital": self.periodo_orbital,
            "gravedad": self.gravedad,
            "poblacion": self.poblacion,
            "clima": self.clima,
            "terreno": self.terreno,
            "superfice_acuatica": self.superfice_acuatica,
            "creacion": self.creacion,
            "editado": self.editado,
            "nombre": self.nombre
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250))
    Favoritos = db.relationship('Favoritos', backref='Usuario', uselist=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "Favoritos": self.Favoritos
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def get_favotiros(self):
    #     Favoritos = list(map(lambda Favoritos: Favoritos.serialize(), self.Favoritos))
    #     return Favoritos


class Favoritos(db.Model):
    __tablename__ = 'Favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    planeta_id = db.Column(db.Integer, db.ForeignKey('Planeta.id'))
    personajes_id = db.Column(db.Integer, db.ForeignKey('Personajes.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey(
        'Usuario.id'), primary_key=True)

    def serialize(self):
        return {
            "id": self.id,
            "planeta_id": self.planeta_id,
            "personajes_id": self.personajes_id,
            "Usuario_id": self.usuario_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


# class Favoritos(db.Model):
#     __tablename__ = 'Favoritos'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = db.Column(db.Integer, primary_key=True)
#     planeta_id = db.Column(db.Integer, db.ForeignKey('Planeta.id'))
#     personajes_id = db.Column(db.Integer, db.ForeignKey('Personajes.id'))
#     usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'))
#     usuario = db.relationship(Usuario)
#     planetas = db.relationship(Planeta)
#     personajes = db.relationship(Personajes)

#     def serialize(self):
#         return {
#             "id": self.id,
#             "planeta_id": self.planeta_id,
#             "personajes_id": self.personajes_id,
#             "usuario_id": self.usuario_id
#         }
