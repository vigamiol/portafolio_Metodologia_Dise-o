from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class Asignatura:
    def __init__(self, nombre: str, codigo: str, creditos: int, tipo: str = "General"):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = tipo  # "Pregrado", "Magister", "Doctorado", "General"

    def __repr__(self):
        return f"{self.nombre} ({self.codigo}, {self.creditos} créditos, {self.tipo})"

class Alumno(ABC):
    def __init__(self, nombre: str, edad: int, rut: str, fecha_nacimiento: str):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.asignaturas: List[Asignatura] = []

    def agregar_asignatura(self, asignatura: Asignatura):
        self.asignaturas.append(asignatura)

    def descargar_notas(self):
        print(f"Descargando notas de {self.nombre} para asignaturas: {[a.nombre for a in self.asignaturas]}")

    @abstractmethod
    def actividades(self):
        pass

class Alumni(Alumno):
    def actividades(self):
        return ["No estudia ni hace ayudantias"]

class EstudianteNoAyudante(Alumno):
    def actividades(self):
        return ["Estudiar"]

class EstudianteAyudante(Alumno):
    def actividades(self):
        return ["Estudiar", "Ayudantía"]

class EstudianteMagister(Alumno):
    def actividades(self):
        return ["Estudiar", "Hacer clases"]

class EstudianteDoctorado(Alumno):
    def actividades(self):
        return ["Estudiar", "Hacer clases", "Investigar"]


class DB:
    alumnos: Dict[str, Alumno] = {}
    asignaturas: Dict[str, Asignatura] = {}

    @classmethod
    def insertar_alumno(cls, alumno: Alumno):
        cls.alumnos[alumno.rut] = alumno
        print(f"Alumno insertado: {alumno.nombre} ({alumno.rut})")

    @classmethod
    def obtener_alumno(cls, rut: str) -> Optional[Alumno]:
        return cls.alumnos.get(rut)

    @classmethod
    def modificar_alumno(cls, rut: str, **kwargs):
        alumno = cls.alumnos.get(rut)
        if alumno:
            for key, value in kwargs.items():
                if hasattr(alumno, key):
                    setattr(alumno, key, value)
            print(f"Alumno modificado: {alumno.nombre} ({alumno.rut})")

    @classmethod
    def eliminar_alumno(cls, rut: str):
        if rut in cls.alumnos:
            del cls.alumnos[rut]
            print(f"Alumno eliminado: {rut}")

    @classmethod
    def insertar_asignatura(cls, asignatura: Asignatura):
        cls.asignaturas[asignatura.codigo] = asignatura
        print(f"Asignatura insertada: {asignatura.nombre} ({asignatura.codigo})")

    @classmethod
    def obtener_asignatura(cls, codigo: str) -> Optional[Asignatura]:
        return cls.asignaturas.get(codigo)

    @classmethod
    def modificar_asignatura(cls, codigo: str, **kwargs):
        asignatura = cls.asignaturas.get(codigo)
        if asignatura:
            for key, value in kwargs.items():
                if hasattr(asignatura, key):
                    setattr(asignatura, key, value)
            print(f"Asignatura modificada: {asignatura.nombre} ({asignatura.codigo})")

    @classmethod
    def eliminar_asignatura(cls, codigo: str):
        if codigo in cls.asignaturas:
            del cls.asignaturas[codigo]
            print(f"Asignatura eliminada: {codigo}")


if __name__ == "__main__":
    # Crear asignaturas
    a1 = Asignatura("Matemáticas", "MAT101", 6, "Pregrado")
    a2 = Asignatura("Investigación Avanzada", "INV501", 8, "Doctorado")
    a3 = Asignatura("Gestión de Proyectos", "GES301", 5, "Magister")
    DB.insertar_asignatura(a1)
    DB.insertar_asignatura(a2)
    DB.insertar_asignatura(a3)

    # Crear alumnos
    alumno1 = EstudianteNoAyudante("Ana Pérez", 20, "12345678-9", "2004-01-01")
    alumno2 = EstudianteAyudante("Luis Soto", 22, "98765432-1", "2002-05-10")
    alumno3 = EstudianteMagister("María López", 25, "11223344-5", "1999-03-15")
    alumno4 = EstudianteDoctorado("Carlos Ruiz", 30, "55667788-0", "1994-07-20")
    alumno5 = Alumni("Pedro Torres", 28, "22334455-6", "1996-11-11")

    DB.insertar_alumno(alumno1)
    DB.insertar_alumno(alumno2)
    DB.insertar_alumno(alumno3)
    DB.insertar_alumno(alumno4)
    DB.insertar_alumno(alumno5)

    # Asignar asignaturas
    alumno1.agregar_asignatura(a1)
    alumno2.agregar_asignatura(a1)
    alumno3.agregar_asignatura(a3)
    alumno4.agregar_asignatura(a2)

    # Descargar notas
    alumno1.descargar_notas()
    alumno4.descargar_notas()

    # Modificar alumno
    DB.modificar_alumno("12345678-9", nombre="Ana P. Pérez")

    # Eliminar asignatura
    DB.eliminar_asignatura("GES301")