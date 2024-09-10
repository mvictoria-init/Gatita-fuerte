from conexion import Conexion
from usuario import Usuario

class UsuarioDao:
    
    CONSULTAR_DB = 'SELECT * FROM usuario;'
    INSERTAR = 'INSERT INTO usuario(cedula, nombre, apellido, cumpleaños, nombreapp, contraseña, administrador) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    ACTUALIZAR = 'UPDATE usuario SET cedula=%s, nombre=%s, apellido=%s, cumpleaños=%s, nombreapp=%s, contraseña=%s, administrador=%s WHERE id=%s;'
    SELECCIONAR_ID = 'SELECT * FROM usuario WHERE id=%s;'
    ELIMINAR = 'DELETE FROM usuario WHERE id=%s;'
    PERMISO_DE_ACCESO = 'SELECT * FROM usuario WHERE nombreapp=%s;'
    
    @classmethod
    def acceder_bd(cls, usuario):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (usuario.nombreapp,)
            cursor.execute(cls.PERMISO_DE_ACCESO, valores)
            registro = cursor.fetchone()
            usuario = Usuario(registro[0], registro[1], registro[2], registro[3], 
                                  registro[4], registro[5], registro[6], registro[7])
            return (registro[5], registro[6], registro[7])
        except Exception as e:
            print(f'Ocurrio un error al dar acceso al usuario: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def eliminar_bd(cls, usuario):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (usuario.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar el usuario: {e}')
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
            usuario = Usuario(registro[0], registro[1], registro[2], registro[3], 
                                  registro[4], registro[5], registro[6], registro[7])
            return usuario
        except Exception as e:
            print(f'Ocurrio un error al seleccionar usuario: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def actualizar_bd(cls, usuario):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (usuario.cedula, usuario.nombre, usuario.apellido, usuario.cumpleaños, usuario.nombreapp, usuario.contraseña, usuario.administrador, usuario.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar usuario: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def insertar_bd(cls, usuario):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (usuario.cedula, usuario.nombre, usuario.apellido, usuario.cumpleaños, usuario.nombreapp, usuario.contraseña, usuario.administrador)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al agregar usuario: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
                
    @classmethod
    def consultar_bd(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.CONSULTAR_DB)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2], registro[3], 
                                  registro[4], registro[5], registro[6], registro[7])
                usuarios.append(usuario)
            return usuarios
        except Exception as e:
            print(f'Ocurrio un error al seleccionar usuarios: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    
    # # Seleccionar usuarios
    # ver_usuarios = UsuarioDao.consultar_bd()
    # for cliente in ver_usuarios:
    #     print(cliente)
    
    # insertar usuario
    # usuario1= Usuario(cedula='31526889', nombre='Jesus', apellido='Manuel', cumpleaños='2004-12-21', nombreapp='yisus', contraseña='11', administrador='1')
    # usuario_insertado = UsuarioDao.insertar_bd(usuario1)
    # print(f'Usuario insertados: {usuario_insertado}')
    
    # actualizar usuario
    # usuario2= Usuario(cedula='15152689', nombre='Violeta', apellido='Violet', cumpleaños='2014-09-21', nombreapp='bi', contraseña='1', administrador='1', id=7)
    # usuario_actualizado = UsuarioDao.actualizar_bd(usuario2)
    # print(f'Usuario actualizado: {usuario_actualizado}')
    
    # dar acceso a usuario
    usuario3= Usuario(nombreapp='aaa')
    usuario_acceder = UsuarioDao.acceder_bd(usuario3)
    print(f'Usuario accedio de forma exitosa: {usuario_acceder}')
    