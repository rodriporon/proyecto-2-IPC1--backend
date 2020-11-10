class Playlist:
    
    def __init__(self, propietario, idCancion):
        self.propietario = propietario
        self.idCancion = idCancion

    def getPropietario(self):
        return self.propietario

    def getIdCancion(self):
        return self.idCancion

    def setPropietario(self, propietario):
        self.propietario = propietario

    def setIdCancion(self, idCancion):
        self.idCancion = idCancion
