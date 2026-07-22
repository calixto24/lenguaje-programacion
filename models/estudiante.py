from dataclasses import dataclass, field

@dataclass
class Estudiante:
    codigo: str
    nombre: str
    carrera: str
    ciclo: int
    edad: int
    genero: str

    nota1: float
    nota2: float
    nota3: float
    nota4: float

    asistencia: int

    promedio: float = field(init=False)

    def __post_init__(self):
        self.promedio = self.calcular_promedio()

    def calcular_promedio(self) -> float:
        return round(
            (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4,
            2
        )

    def aprobo(self) -> bool:
        return self.promedio >= 11

    def obtener_notas(self) -> list:
        return [
            self.nota1,
            self.nota2,
            self.nota3,
            self.nota4
        ]

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "carrera": self.carrera,
            "ciclo": self.ciclo,
            "edad": self.edad,
            "genero": self.genero,
            "nota1": self.nota1,
            "nota2": self.nota2,
            "nota3": self.nota3,
            "nota4": self.nota4,
            "promedio": self.promedio,
            "asistencia": self.asistencia
        }

    def __str__(self):
        return (
            f"{self.codigo} | "
            f"{self.nombre} | "
            f"Promedio: {self.promedio} | "
            f"Asistencia: {self.asistencia}%"
        )