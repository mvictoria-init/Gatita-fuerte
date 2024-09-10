from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente' #
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'#
    INSERTAR = 'INSERT INTO cliente(cedula, nombre, apellido, cumpleaños, membresia, tipo_membresia, fecha_suscripcion) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET cedula=%s, nombre=%s, apellido=%s, cumpleaños=%s, membresia=%s, tipo_membresia=%s, fecha_suscripcion=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4], 
                                  registro[5], registro[6], registro[7])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def seleccionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.SELECCIONAR_ID, valores)
            registro = cursor.fetchone()
            # mapeo clase-tabla cliente
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3], registro[4], 
                                  registro[5], registro[6], registro[7])
            return cliente
        except Exception as e:
            print(f'Ocurrio al seleccionar el cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.cedula, cliente.nombre, cliente.apellido, cliente.cumpleaños, cliente.membresia, cliente.tipo_membresia, cliente.fecha_suscripcion)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.cedula, cliente.nombre, cliente.apellido, cliente.cumpleaños, cliente.membresia, cliente.tipo_membresia, cliente.fecha_suscripcion, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

# if __name__ == '__main__':
    # Seleccionar clientes
    # clientes = ClienteDAO.seleccionar()
    # for cliente in clientes:
    #     print(cliente)
    
    # insertar cliente 
    # cliente = Cliente(cedula='15278445', nombre='Lisa', apellido='Lares', cumpleaños='1997-04-28', 
    #                   membresia=1554, tipo_membresia='mensual', fecha_suscripcion='1997-04-28')
    # insertar_cliente = ClienteDAO.insertar(cliente)
    # print(f'Cliente insertado {insertar_cliente}... {cliente}')
    