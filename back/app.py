from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)   # se relaciona con el final. Objeto flask que nos permite crear la conexión a la BD y los modelos. además de la manipulación.
CORS(app)               # Se relaciona con el Front. 

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/crud_audiovisuales'
#Driver de la BD user:clave@URLBBDD/nombreBBDD
# 'mysql+pymsql' es el driver de la bd. 
#Luego de :// se consigo en phpmyadmin en usuario.
# Luego de usuario: iria contraseña, como no tengo va el url. y luego el nombre de bd.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Esto es para que no trackee las modificaciones.


#creando instancias de SQLAlchemy y de Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

#BBDD 
class Contenido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    tipo = db.Column(db.String(15)) #Pasar serie o pelicula
    genero = db.Column(db.String(100)) #Si es posible, darle otra clase y hacer un n:m
    sinopsis = db.Column(db.String(1000))
    imagen = db.Column(db.String(400))
    valoracion = db.Column(db.Float())  #valor a comparar con valoracion_max
    valoracion_max = db.Column(db.Float()) #darle numero fijo (intentar no pasarle valor ya que es auto.)

    def __init__(self, titulo, tipo,genero, sinopsis, imagen, valoracion, valoracion_max=5.0):
        self.titulo = titulo
        self.tipo = tipo
        self.genero = genero
        self.sinopsis = sinopsis
        self.imagen = imagen
        self.valoracion = valoracion
        self.valoracion_max = valoracion_max


#crear el contexto de la bbdd

with app.app_context():  #(app_context) viene de Flask.
    db.create_all() #Esto ejecuta la creación de las tablas.

class ContenidoSchema(ma.Schema):
    class Meta:
        fields=('id','titulo','tipo','genero','sinopsis','imagen','valoracion','valoracion_max')


contenido_schema = ContenidoSchema()  
contenidos_schema = ContenidoSchema(many=True)


#Definir rutas
  
@app.route('/contenidos', methods=['GET'])

def get_contenidos():
    contenidos = Contenido.query.all()
    resultado = contenidos_schema.dump(contenidos)
    return jsonify(resultado)


@app.route('/contenidos/<id>', methods=['GET'])
def get_contenido(id):
    contenido = Contenido.query.get(id)
    return contenido_schema.jsonify(contenido)


@app.route('/contenidos/<id>', methods=['DELETE'])
def delete_contenido(id):
    contenido = Contenido.query.get(id)
    db.session.delete(contenido)
    db.session.commit() #es necesario el commit para que persista el dato.
    return contenido_schema.jsonify(contenido)


@app.route('/contenidos', methods=['POST'])
def create_contenido(): 
    titulo = request.json['titulo']  #Te llega el dato del front (Form) y lo guardas.
    tipo = request.json['tipo']
    genero = request.json['genero']
    sinopsis = request.json['sinopsis']
    imagen = request.json['imagen']
    valoracion = request.json['valoracion']
    valoracion_max = request.json['valoracion_max'] #Preguntar si es necesario si se pasa un dato por defecto.

    nuevo_contenido = Contenido (titulo,tipo,genero,sinopsis,imagen,valoracion,valoracion_max)
    db.session.add(nuevo_contenido) #Agregamos el nuevo contenido a la db.
    db.session.commit() 
    return contenido_schema.jsonify(nuevo_contenido)

@app.route('/contenidos/<id>', methods=['PUT'])
def update_contenido(id):
    contenido = Contenido.query.get(id)

    #Datos traido a actualizar
    titulo = request.json['titulo']  
    tipo = request.json['tipo']
    genero = request.json['genero']
    sinopsis = request.json['sinopsis']
    imagen = request.json['imagen']
    valoracion = request.json['valoracion']
    valoracion_max = request.json['valoracion_max'] #Preguntar si es necesario si se pasa un dato por defecto.
    #Se actualiza
    contenido.titulo = titulo
    contenido.tipo = tipo
    contenido.genero = genero
    contenido.sinopsis = sinopsis
    contenido.imagen = imagen
    contenido.valoracion = valoracion
    contenido.valoracion_max = valoracion_max
    
    db.session.commit()
    return contenido_schema.jsonify(contenido)


if __name__ == '__main__':
    app.run(debug=True, port=5000) 






