"""Base de Datos - Creación de Clase en ORM"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Socio(Base):
    """Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, unico)
        - dni: entero (unico)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'

    id_socio = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    dni = Column(Integer, unique=True, nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False) 

    def __eq__(self, other):
        if isinstance(other, Socio):
            return (self.id_socio == other.id_socio and
                    self.dni == other.dni and
                    self.nombre == other.nombre and
                    self.apellido == other.apellido)
        return False

    def __hash__(self):
        return hash((self.id_socio, self.dni, self.nombre, self.apellido))

