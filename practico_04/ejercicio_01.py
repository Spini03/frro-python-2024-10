"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3
import pymysql

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    # Completar

    conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="Git231653*", db="practico4" )

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Persona (
            IdPersona INTEGER PRIMARY KEY AUTO_INCREMENT,
            Nombre TEXT,
            FechaNacimiento DATETIME,
            DNI INTEGER,
            Altura INTEGER
        )
    ''')

    conn.commit()
    conn.close()
    cursor.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    # Completar

    conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="Git231653*", db="practico4" )

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS Persona")

    conn.commit()
    conn.close()
    cursor.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
