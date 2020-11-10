class Comentario:
    def __init__(self, usuario, idCancion, comentario):
        self.usuario = usuario
        self.idCancion = idCancion
        self.comentario = comentario

    def getUsuario(self):
        return self.usuario

    def getIdCancion(self):
        return self.idCancion

    def getComentario(self):
        return self.comentario

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setIdCancion(self, idCancion):
        self.idCancion = idCancion

    def setComentario(self, comentario):
        self.comentario = comentario