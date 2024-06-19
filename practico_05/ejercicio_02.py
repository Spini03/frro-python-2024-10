"""Base de Datos - ORM"""

from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional

DATABASE_URL = 'sqlite:///socios.db'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

class DatosSocio():

    def __init__(self):
        Base.metadata.create_all(bind=engine)

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        session: Session = SessionLocal()
        
        try:
            socio = session.query(Socio).filter(Socio.id_socio == id_socio).first()
            return socio
        finally:
            session.close()

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        session: Session = SessionLocal()
        try:
            socio = session.query(Socio).filter(Socio.dni == dni_socio).first()
            return socio
        finally:
            session.close()
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        
        session: Session = SessionLocal()
        try:
            socios = session.query(Socio).all()
            return socios
        finally:
            session.close()


    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        session: Session = SessionLocal()

        try:
            session.query(Socio).delete()
            session.commit()
            return True
        except:
            session.rollback()
            return False
        finally:
            session.close()

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""

        session: Session = SessionLocal()
        try:
            session.add(socio)
            session.commit()
            session.refresh(socio)  # Actualiza la instancia con la información de la base de datos
            return socio
        except:
            session.rollback()
            raise
        finally:
            session.close()


    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        session: Session = SessionLocal()
        try:
            socio = session.query(Socio).filter(Socio.id_socio == id_socio).first()
            if socio:
                session.delete(socio)
                session.commit()
                return True
            else:
                return False
        except:
            session.rollback()
            raise
        finally:
            session.close()


    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        session: Session = SessionLocal()
        try:
            db_socio = session.merge(socio)
            session.commit()
            session.refresh(db_socio)  # Actualiza la instancia con la información de la base de datos
            return socio
        except:
            session.rollback()
            raise
        finally:
            session.close()
    
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        session: Session = SessionLocal()
        try:
            count = session.query(Socio).count()
            return count
        finally:
            session.close()



# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id_socio > 0

# Test Baja
assert datos.baja(socio.id_socio) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id_socio) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id_socio)
assert socio_3_modificado.id_socio == socio_3.id_socio
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN