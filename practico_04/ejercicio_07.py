"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime

import pymysql

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    # Completar
    conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="Git231653*", db="practico4" )

    cursor = conn.cursor()

    resultado = buscar_persona(id_persona)
    if not resultado:
        return False
    
    cursor.execute("SELECT * FROM PersonaPeso WHERE IdPersona = %s AND Fecha > %s", (id_persona, fecha))
    if cursor.fetchone():
        print("Error: Ya existe un registro de fecha posterior para esta persona.")
        return False

    values = (id_persona, fecha, peso)

    cursor.execute("INSERT INTO PersonaPeso (IdPersona, Fecha, Peso) VALUES (%s, %s, %s)", values)

    conn.commit()

    print(f"Nuevo peso de persona registrado en persona con id {id_persona}")

    print(f"Fecha: {fecha}, Peso: {peso}")

    conn.close()
    cursor.close()

    return id_persona


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
