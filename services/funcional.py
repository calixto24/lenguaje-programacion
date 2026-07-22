from functools import reduce
from models.estudiante import Estudiante

class FuncionalAcademico:

    @staticmethod
    def obtener_promedios(estudiantes: list[Estudiante]) -> list[float]:
        """Extrae la lista de promedios de los estudiantes."""
        return list(map(lambda e: e.promedio, estudiantes))

    @staticmethod
    def obtener_nombres(estudiantes: list[Estudiante]) -> list[str]:
        """Extrae la lista de nombres de los estudiantes."""
        return list(map(lambda e: e.nombre, estudiantes))

    @staticmethod
    def obtener_carreras(estudiantes: list[Estudiante]) -> list[str]:
        """Extrae la lista de carreras a las que pertenecen los estudiantes."""
        return list(map(lambda e: e.carrera, estudiantes))

    @staticmethod
    def obtener_asistencias(estudiantes: list[Estudiante]) -> list[float]:
        """Extrae la lista de porcentajes de asistencia."""
        return list(map(lambda e: e.asistencia, estudiantes))

    @staticmethod
    def estudiantes_por_carrera(estudiantes: list[Estudiante], carrera: str) -> list[Estudiante]:
        """Filtra estudiantes perteneciente a una carrera específica."""
        return list(filter(lambda e: e.carrera.lower() == carrera.lower(), estudiantes))

    @staticmethod
    def estudiantes_mayores_edad(estudiantes: list[Estudiante]) -> list[Estudiante]:
        """Filtra estudiantes que tienen 18 años o más."""
        return list(filter(lambda e: e.edad >= 18, estudiantes))

    @staticmethod
    def estudiantes_menores_edad(estudiantes: list[Estudiante]) -> list[Estudiante]:
        """Filtra estudiantes menores de 18 años."""
        return list(filter(lambda e: e.edad < 18, estudiantes))

    @staticmethod
    def estudiantes_por_ciclo(estudiantes: list[Estudiante], ciclo: int) -> list[Estudiante]:
        """Filtra estudiantes pertenecientes a un ciclo determinado."""
        return list(filter(lambda e: e.ciclo == ciclo, estudiantes))

    @staticmethod
    def cantidad_estudiantes(estudiantes: list[Estudiante]) -> int:
        """Cuenta el total de estudiantes usando reduce."""
        return reduce(lambda acc, _: acc + 1, estudiantes, 0)

    @staticmethod
    def suma_promedios(estudiantes: list[Estudiante]) -> float:
        """Suma todos los promedios de la lista de estudiantes."""
        return reduce(
            lambda acumulador, estudiante: acumulador + estudiante.promedio,
            estudiantes,
            0.0
        )

    @staticmethod
    def promedio_general(estudiantes: list[Estudiante]) -> float:
        """Calcula el promedio general del grupo de estudiantes."""
        if not estudiantes:
            return 0.0
            
        suma = FuncionalAcademico.suma_promedios(estudiantes)
        total = FuncionalAcademico.cantidad_estudiantes(estudiantes)
        
        return round(suma / total, 2)