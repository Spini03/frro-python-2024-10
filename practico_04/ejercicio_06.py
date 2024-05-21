"""Base de Datos SQL - Creación de tablas auxiliares"""

import pymysql
from ejercicio_01 import borrar_tabla, crear_tabla


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    # Completar
    conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="Git231653*", db="practico4" )

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS PersonaPeso (
            IdPersona INT,
            Fecha DATETIME,
            Peso INT,
            FOREIGN KEY (IdPersona) REFERENCES Persona(IdPersona)
        );
    ''')

    conn.commit()
    conn.close()
    cursor.close()


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    # Completar

    conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="Git231653*", db="practico4" )

    cursor = conn.cursor()

    cursor.execute("DROP TABLE PersonaPeso")

    conn.commit()
    conn.close()
    cursor.close()


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
