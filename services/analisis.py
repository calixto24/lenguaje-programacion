import numpy as np
import pandas as pd

from models.estudiante import Estudiante


class AnalizadorAcademico:
    def __init__(self, estudiantes: list[Estudiante]):
        self.estudiantes = estudiantes

        self.df = pd.DataFrame(
            [estudiante.to_dict() for estudiante in estudiantes]
        )

    def promedio_general(self) -> float:
        return round(self.df["promedio"].mean(), 2)

    def mediana(self) -> float:
        return round(self.df["promedio"].median(), 2)

    def desviacion_estandar(self) -> float:
        return round(np.std(self.df["promedio"]), 2)

    def varianza(self) -> float:
        return round(np.var(self.df["promedio"]), 2)

    def nota_maxima(self) -> float:
        return self.df["promedio"].max()

    def nota_minima(self) -> float:
        return self.df["promedio"].min()

    def total_estudiantes(self) -> int:
        return len(self.df)

    def aprobados(self) -> int:
        return len(
            self.df[self.df["promedio"] >= 11]
        )

    def desaprobados(self) -> int:
        return len(
            self.df[self.df["promedio"] < 11]
        )

    def promedio_por_carrera(self):
        return (
            self.df
            .groupby("carrera")["promedio"]
            .mean()
            .round(2)
        )

    def promedio_por_ciclo(self):
        return (
            self.df
            .groupby("ciclo")["promedio"]
            .mean()
            .round(2)
        )

    def estudiante_destacado(self):
        indice = self.df["promedio"].idxmax()
        return self.df.loc[indice]

    def estudiante_menor_rendimiento(self):
        indice = self.df["promedio"].idxmin()
        return self.df.loc[indice]

    def resumen(self):

        return {
            "Promedio General": self.promedio_general(),
            "Mediana": self.mediana(),
            "Desviación": self.desviacion_estandar(),
            "Varianza": self.varianza(),
            "Nota Máxima": self.nota_maxima(),
            "Nota Mínima": self.nota_minima(),
            "Aprobados": self.aprobados(),
            "Desaprobados": self.desaprobados(),
            "Total": self.total_estudiantes()
        }