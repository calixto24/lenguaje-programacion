from dataclasses import dataclass

@dataclass
class Estudiante:
    codigo: str
    nombre: str
    sexo: str
    edad: int
    carrera: str
    ciclo: int
    promedio: float
    asistencia: int
    ingreso_familiar: float
    dependientes: int
    trabaja: bool
    tipo_colegio: str
    discapacidad: bool
    orfandad: bool
    departamento: str
    provincia: str
    zona: str

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "sexo": self.sexo,
            "edad": self.edad,
            "carrera": self.carrera,
            "ciclo": self.ciclo,
            "promedio": self.promedio,
            "asistencia": self.asistencia,
            "ingreso_familiar": self.ingreso_familiar,
            "dependientes": self.dependientes,
            "trabaja": self.trabaja,
            "tipo_colegio": self.tipo_colegio,
            "discapacidad": self.discapacidad,
            "orfandad": self.orfandad,
            "departamento": self.departamento,
            "provincia": self.provincia,
            "zona": self.zona
        }

    def __str__(self):

        return (
            f"{self.codigo} | "
            f"{self.nombre} | "
            f"Promedio: {self.promedio} | "
            f"Ingreso: S/. {self.ingreso_familiar:.2f}"
        )