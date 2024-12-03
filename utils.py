from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calcular_edad(fecha_nacimiento):
    """Calcula la edad de una persona a partir de su fecha de nacimiento.

    Args:
        fecha_nacimiento (str): Fecha de nacimiento en formato 'AAAA-MM-DD'.

    Returns:
        int: Edad de la persona.
    """

    hoy = datetime.now()
    if type(fecha_nacimiento) is str:
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def calcular_prox_pago(tipo_membresia: str, fecha_suscripcion):
    print(tipo_membresia)
    if tipo_membresia == 'mensual':
        mes=1
    if tipo_membresia == 'trimestral':
        mes=3
    if tipo_membresia == 'anual':
        mes=12
        
    if type(fecha_suscripcion) is str:
        fecha_suscripcion = datetime.strptime(fecha_suscripcion, '%Y-%m-%d')
    return fecha_suscripcion + relativedelta(months=mes)
    
if __name__ == '__main__':
    # Ejemplo de uso:
    fecha_nacimiento = "1994-03-21"
    edad = calcular_edad(fecha_nacimiento)
    print(f"Tienes {edad} años.")