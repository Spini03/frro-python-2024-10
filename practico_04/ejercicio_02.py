"""Base de Datos SQL - Alta"""

import datetime

import pymysql
from ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    """Implementar la funcion agregar_persona, que inserte un registro en la 
    tabla Persona y devuelva los datos ingresados y el id del nuevo registro."""
    # Completar
    conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="Git231653*", db="practico4" )

    cursor = conn.cursor()

    values = (nombre, nacimiento, dni, altura)

    cursor.execute("INSERT INTO Persona (Nombre, FechaNacimiento, DNI, Altura) VALUES (%s, %s, %s, %s)", values)

    conn.commit()

    nuevo_id = cursor.lastrowid

    print(f"Nueva persona registrada con id {nuevo_id}")

    print(f"Nombre: {nombre}, Fecha de nacimiento: {nacimiento}, DNI: {dni}, Altura: {altura}")

    conn.close()
    cursor.close()

    return nuevo_id



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
