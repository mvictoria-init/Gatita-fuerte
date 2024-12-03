from mysql.connector import pooling
from mysql.connector import Error
from decouple import config


class Conexion:

    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Se crea el objeto pool
            print(config('POOL_NAME'))
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=config('POOL_NAME'),
                    pool_size=int(config('POOL_SIZE')),
                    host=config('HOST'),
                    port=int(config('DB_PORT')),
                    database=config('DATABASE'),
                    user=config('USERNAME'),
                    password=config('PASSWORD')
                )
                #print(f'Nombre del pool: {cls.pool.pool_name}')
                #print(f'Tamanio del pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__ == '__main__':
    # Creacion del objeto pool
    #pool = Conexion.obtener_pool()
    #print(pool)
    # Obtener un objeto conexion
    cnx1 = Conexion.obtener_conexion()
    print(cnx1)
    Conexion.liberar_conexion(cnx1)
