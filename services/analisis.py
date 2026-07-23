import numpy as np
import pandas as pd

from models.estudiante import Estudiante


class AnalizadorBecas:

    def __init__(self, estudiantes: list[Estudiante]):
        self.estudiantes = estudiantes

        self.df = pd.DataFrame(
            [estudiante.to_dict() for estudiante in estudiantes]
        )

    def total_estudiantes(self) -> int:
        return len(self.df)

    def promedio_general(self) -> float:
        return round(np.mean(self.df["promedio"]), 2)

    def mediana_promedios(self) -> float:
        return round(np.median(self.df["promedio"]), 2)

    def desviacion_promedios(self) -> float:
        return round(np.std(self.df["promedio"]), 2)

    def varianza_promedios(self) -> float:
        return round(np.var(self.df["promedio"]), 2)

    def promedio_maximo(self) -> float:
        return np.max(self.df["promedio"])

    def promedio_minimo(self) -> float:
        return np.min(self.df["promedio"])

    def ingreso_promedio(self) -> float:
        return round(np.mean(self.df["ingreso_familiar"]), 2)

    def ingreso_mediano(self) -> float:
        return round(np.median(self.df["ingreso_familiar"]), 2)

    def ingreso_maximo(self) -> float:
        return np.max(self.df["ingreso_familiar"])

    def ingreso_minimo(self) -> float:
        return np.min(self.df["ingreso_familiar"])

    def desviacion_ingresos(self) -> float:
        return round(np.std(self.df["ingreso_familiar"]), 2)

    def varianza_ingresos(self) -> float:
        return round(np.var(self.df["ingreso_familiar"]), 2)

    def percentil_25_ingresos(self) -> float:
        return round(
            np.percentile(self.df["ingreso_familiar"], 25),
            2
        )

    def percentil_75_ingresos(self) -> float:
        return round(
            np.percentile(self.df["ingreso_familiar"], 75),
            2
        )

    def promedio_dependientes(self) -> float:
        return round(
            np.mean(self.df["dependientes"]),
            2
        )

    def maximo_dependientes(self) -> int:
        return int(
            np.max(self.df["dependientes"])
        )

    def promedio_por_carrera(self):
        return (
            self.df
            .groupby("carrera")["promedio"]
            .mean()
            .round(2)
        )

    def ingreso_promedio_por_carrera(self):
        return (
            self.df
            .groupby("carrera")["ingreso_familiar"]
            .mean()
            .round(2)
        )

    def promedio_por_departamento(self):
        return (
            self.df
            .groupby("departamento")["promedio"]
            .mean()
            .round(2)
        )

    def ingreso_promedio_por_departamento(self):
        return (
            self.df
            .groupby("departamento")["ingreso_familiar"]
            .mean()
            .round(2)
        )

    def estudiantes_por_carrera(self):
        return self.df["carrera"].value_counts()

    def estudiantes_por_departamento(self):
        return self.df["departamento"].value_counts()

    def estudiantes_por_genero(self):
        return self.df["sexo"].value_counts()

    def estudiantes_por_tipo_colegio(self):
        return self.df["tipo_colegio"].value_counts()

    def estudiantes_por_zona(self):
        return self.df["zona"].value_counts()

    def estudiantes_que_trabajan(self):
        return self.df["trabaja"].value_counts()

    def resumen(self):

        return {
            "Total de estudiantes": self.total_estudiantes(),

            "Promedio general": self.promedio_general(),
            "Mediana de promedios": self.mediana_promedios(),
            "Desviación estándar": self.desviacion_promedios(),
            "Varianza": self.varianza_promedios(),
            "Promedio máximo": self.promedio_maximo(),
            "Promedio mínimo": self.promedio_minimo(),

            "Ingreso promedio": self.ingreso_promedio(),
            "Ingreso mediano": self.ingreso_mediano(),
            "Ingreso máximo": self.ingreso_maximo(),
            "Ingreso mínimo": self.ingreso_minimo(),

            "Promedio de dependientes": self.promedio_dependientes()
        }