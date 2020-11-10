from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

from Usuarios import Usuario
from Canciones import Cancion
from Playlists import Playlist
from Comentarios import Comentario

app = Flask(__name__)
CORS(app)

Comentarios = []
Playlists = []
Usuarios = []
Canciones = []
contadorcanciones = 0



Usuarios.append(Usuario('Rodri','Poron','amrodri','1234','Administrador'))
Usuarios.append(Usuario('Usuario','Maestro','admin','admin', 'Administrador'))
Usuarios.append(Usuario('Alisson','Poron','alisson','1234', 'Cliente'))

@app.route('/', methods=['GET'])
def index():
    print("Ruta inicial")
    return("Ruta inicial")

@app.route('/usuarios', methods=['GET'])
def obtenerUsuarios():
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        Dato = {
            'nombre': usuario.getNombre(), 
            'apellido': usuario.getApellido(), 
            'usuario': usuario.getUsuario(),
            'rol' : usuario.getRol()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/usuarios/<string:nombre>', methods=['GET'])
def obtenerUsuario(nombre):
    global Usuarios
    for usuario in Usuarios:
        if usuario.getUsuario() == nombre:
            Dato = {
                'nombre': usuario.getNombre(), 
                'apellido': usuario.getApellido(),
                'usuario': usuario.getUsuario(),
                'password': usuario.getPassword(),
                'rol': usuario.getRol()
                }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/usuarios/<string:nombre>', methods=['PUT'])
def actualizarUsuario(nombre):
    global Usuarios
    for i in range(len(Usuarios)):
        if nombre == Usuarios[i].getUsuario():
            Usuarios[i].setNombre(request.json['nombre'])
            Usuarios[i].setApellido(request.json['apellido'])
            Usuarios[i].setUsuario(request.json['usuario'])
            Usuarios[i].setPassword(request.json['password'])
            break
    return jsonify({'message':'Los datos se actualizaron satisfactoriamente'})

@app.route('/usuarios/<string:usuario>', methods=['DELETE'])
def eliminarPersona(usuario):
    global Usuarios
    for i in range(len(Usuarios)):
        if usuario == Usuarios[i].getUsuario():
            #En este caso, para eliminar un objeto de un arreglo utilizamos
            #La palabra reservada del arreglo[indice]
            del Usuarios[i]
            break
    return jsonify({'message':'Se eliminó el usuario exitosamente'})

@app.route('/usuarios', methods=['POST'])
def agregarUsuario():
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    username = request.json['usuario']
    password = request.json['password']
    confpassword = request.json['confpassword']
    rol = request.json['rol']
    encontrado = False
    if password != confpassword:
        return jsonify({
            'message': 'Failed',
            'reason': 'Las contraseñas no coinciden'
        })
    for usuario in Usuarios:
        if usuario.getUsuario() == username:
            encontrado = True
            break
    if encontrado:
        return jsonify({
            'message':'Failed',
            'reason':'Este usuario ya existe'
            })
    else:
        nuevo = Usuario(nombre,apellido,username,password,rol)
        Usuarios.append(nuevo)
        return jsonify({
            'message':'Success',
            'reason':'Se registró el usuario'
            })

@app.route('/comentario', methods = ['POST'])
def agregarComentario():
    global Comentarios
    usuario = request.json['usuario']
    idCancion = int(request.json['idCancion'])
    comentario = request.json['comentario']
    nuevo = Comentario(usuario, idCancion, comentario)
    Comentarios.append(nuevo)
    print(idCancion)
    return jsonify({
        'message': 'Success',
        'reason': 'Se envió su comentario'
    })
           


@app.route('/playlist/<string:usuario>', methods=['POST'])
def agregarPlaylist(usuario):
    global Playlists
    idCancion = request.json['idCancion']
    propietario = usuario
    nuevo = Playlist(propietario, idCancion)
    Playlists.append(nuevo)
    return jsonify({
    'message':'Success',
    'reason':'Se agregó la canción a su playlist'
    })

@app.route('/playlist/<string:usuario>', methods=['GET'])
def obtenerPlaylist(usuario):
    global Playlists
    Datos = []
    for playlist in Playlists:
        if usuario == playlist.getPropietario():
            Dato = {
                'idCancion': playlist.getIdCancion(),
                'propietario': playlist.getPropietario()   
            }
            Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)



@app.route('/login', methods=['POST'])
def Login():
    global Usuarios
    username = request.json['usuario']
    password = request.json['password']
    for usuario in Usuarios:
        if usuario.getUsuario() == username and usuario.getPassword() == password and usuario.getRol == 'Administrador':
            Dato = {
                'message': 'Success-admin',
                'usuario': usuario.getUsuario(),
                'rol': usuario.getRol()
            }
            break
        elif usuario.getUsuario() == username and usuario.getPassword() == password:
            Dato = {
                'message': 'Success',
                'usuario': usuario.getUsuario(),
                'rol': usuario.getRol()
                }
            break
        else:
            Dato = {
                'message': 'Failed',
                'usuario': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/comentario/<string:id>', methods=['POST'])
def obtenerComentarioId(id):
    global Comentarios
    Datos = []
    for comen in Comentarios:
        if comen.getIdCancion() == int(id):
            Dato = {
                'usuario': comen.getUsuario(),
                'idCancion': comen.getIdCancion(),
                'comentario': comen.getComentario()
            }
            Datos.append(Dato)
        else:
            Dato = {
                'comentario': ''
            }
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/comentario', methods=['GET'])
def obtenerComentario():
    global Comentarios
    Datos = []
    for comen in Comentarios:
        Dato = {
                'usuario': comen.getUsuario(),
                'idCancion': comen.getIdCancion(),
                'comentario': comen.getComentario()
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/obtenerpassword', methods=['POST'])
def obtenerPassword():
    global Usuarios
    username = request.json['usuario']
    for usuario in Usuarios:
        if usuario.getUsuario() == username:
            Dato = {
                'message': 'Sucess',
                'password': usuario.getPassword()
            }
            break
        else:
            Dato = {
                'message': 'Failed',
                'password': ''
            }
    respuesta = jsonify(Dato)
    return(respuesta)

@app.route('/cancion', methods=['POST'])
def guardarCancion():
    global Canciones, contadorcanciones
    id = contadorcanciones
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']
    nuevo = Cancion(id, nombre, artista, album, fecha, imagen, spotify, youtube)
    Canciones.append(nuevo)
    contadorcanciones += 1
    return jsonify({
            'message':'Success',
            'reason':'Se agrego la cancion'
            })

@app.route('/cancion', methods=['GET'])
def obtenerCanciones():
    global Canciones, contadorcanciones
    Datos = []
    for cancion in Canciones:
        Dato = {
            'id': cancion.getId(),
            'nombre': cancion.getCancion(),
            'artista': cancion.getArtista(),
            'album': cancion.getAlbum(),
            'fecha': cancion.getFecha(),
            'imagen': cancion.getImagen(),
            'spotify': cancion.getSpotify(),
            'youtube': cancion.getYoutube()     
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/cancion/<string:id>', methods=['GET'])
def obtenerCancion(id):
    global Canciones
    DatosM = []
    for cancion in Canciones:
        if cancion.getId() == int(id):
            Datomodificar = {
                'id': cancion.getId(),
                'nombre': cancion.getCancion(),
                'artista': cancion.getArtista(),
                'album': cancion.getAlbum(),
                'fecha': cancion.getFecha(),
                'imagen': cancion.getImagen(),
                'spotify': cancion.getSpotify(),
                'youtube': cancion.getYoutube()     
                }
            DatosM.append(Datomodificar)
            break
    respuesta = jsonify(DatosM)
    return(respuesta)

@app.route('/cancion/<string:id>', methods=['PUT'])
def actualizarCancion(id):
    global Canciones
    for i in range(len(Canciones)):
        if  int(id) == Canciones[i].getId():
            Canciones[i].setCancion(request.json['nombre'])
            Canciones[i].setArtista(request.json['artista'])
            Canciones[i].setAlbum(request.json['album'])
            Canciones[i].setFecha(request.json['fecha'])
            Canciones[i].setImagen(request.json['imagen'])
            Canciones[i].setSpotify(request.json['spotify'])
            Canciones[i].setYoutube(request.json['youtube'])
            break
    return jsonify({'message':'La canción se modificó correctamente'})

@app.route('/cancion/<string:id>', methods=['DELETE'])
def eliminarCancion(id):
    global Canciones
    for i in range(len(Canciones)):
        if int(id) == Canciones[i].getId():
            del Canciones[i]
            break
    return jsonify({'message':'Eliminación satisfactoria'})



if __name__ == "__main__":
    app.run(threaded=True, port=3000, debug=True)


