"""Base de Datos SQL - Baja"""

import datetime

import pymysql

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    # Completar

    conn = pymysql.connect( host="localhost", port=3306, user="root", passwd="Git231653*", db="practico4" )

    cursor = conn.cursor()

    cursor.execute("DELETE FROM Persona WHERE IdPersona = %s", (id_persona,))

    conn.commit()

    filas_afectadas = cursor.rowcount

    conn.close()
    cursor.close()

    return filas_afectadas > 0

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
