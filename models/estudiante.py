from dataclasses import dataclass

@dataclass
class Estudiante:
    codigo: str
    nombre: str
    carrera: str
    ciclo: int
    creditos_matriculados: int
    promedio_ciclo_anterior: float
    asistencia: float
    distrito: str
    edad: int
    sexo: str

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "carrera": self.carrera,
            "ciclo": self.ciclo,
            "creditos_matriculados": self.creditos_matriculados,
            "promedio_ciclo_anterior": self.promedio_ciclo_anterior,
            "asistencia": self.asistencia,
            "distrito": self.distrito,
            "edad": self.edad,
            "sexo": self.sexo
        }