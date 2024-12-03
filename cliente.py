from utils import calcular_edad, calcular_prox_pago
class Cliente:
    def __init__(self, id=None, cedula=None, nombre=None, apellido=None, cumpleaños=None, 
                membresia=None, tipo_membresia=None, fecha_suscripcion=None):
        self.id = id
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.cumpleaños = cumpleaños
        self.membresia = membresia
        self.tipo_membresia = tipo_membresia
        self.fecha_suscripcion = fecha_suscripcion
        self.edad = calcular_edad(cumpleaños)
        self.proximo_pago = calcular_prox_pago(tipo_membresia, fecha_suscripcion)

    
    def __str__(self):
        return (f''' Id: {self.id} - Cédula: {self.cedula}
                        Nombre: {self.nombre} Apellido: {self.apellido} Fecha de nacimiento: {self.cumpleaños}
                        Membresía
                        Número: {self.membresia} Tipo: {self.tipo_membresia} Fecha de inscripción: {self.fecha_suscripcion}
                ''')