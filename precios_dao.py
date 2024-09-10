from conexion import Conexion
from precios import Precios

class PreciosDao:
    
    MOSTRAR = 'SELECT * FROM precios WHERE id=1;'
    ACTUALIZAR = 'UPDATE precios SET mensual=%s, trimestral=%s, anual=%s WHERE id=1;'
    
    @classmethod
    def actualizar_precios(cls, precios):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (precios.mensual, precios.trimestral, precios.anual,)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al seleccionar precios: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def mostrar_precios(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.MOSTRAR)
            registro = cursor.fetchone()
            precios = Precios(registro[0], registro[1], registro[2])
            return precios
        except Exception as e:
            print(f'Ocurrio un error al mostrar precios: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
if __name__ == '__main__':
    
    # mostrar precios
    precio = PreciosDao.mostrar_precios()
    print(precio)
    
    # actualizar precios
    precio1 = Precios(mensual='15', trimestral='45', anual='100')
    actualizar_precio = PreciosDao.actualizar_precios(precio1)
    print(f'Los precios han sido actualizados... {precio1}')
    