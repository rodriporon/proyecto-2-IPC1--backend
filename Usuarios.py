
class Usuario:

    def __init__(self, nombre, apellido, usuario, password, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.rol = rol

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getUsuario(self):
        return self.usuario

    def getPassword(self):
        return self.password

    def getRol(self):
        return self.rol

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setPassword(self, password):
        self.password = password

    def setRol(self, rol):
        self.rol = rol