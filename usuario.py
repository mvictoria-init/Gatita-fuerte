class Usuario:
    def __init__(self, id=None, cedula=None, nombre=None, apellido=None, cumpleaños=None, 
                 nombreapp=None, contraseña=None, administrador=None):
        self.id = id
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.cumpleaños = cumpleaños
        self.nombreapp = nombreapp
        self.contraseña = contraseña
        self.administrador = administrador
    
    def __str__(self):
        return (f''' Id: {self.id} - Cédula: {self.cedula}
                        Nombre: {self.nombre} Apellido: {self.apellido} Fecha de nacimiento: {self.cumpleaños}
                        Nombre de usuario: {self.nombreapp} Contraseña: {self.contraseña} Administrador: {self.administrador}
                ''')