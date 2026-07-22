from pathlib import Path
import pandas as pd
from models.estudiante import Estudiante

class LectorCSV:
    COLUMNAS_OBLIGATORIAS = [
        "codigo",
        "nombre",
        "carrera",
        "ciclo",
        "edad",
        "genero",
        "nota1",
        "nota2",
        "nota3",
        "nota4",
        "asistencia"
    ]

    @staticmethod
    def leer_estudiantes(ruta_csv: str) -> list[Estudiante]:

        ruta = Path( ruta_csv )

        if not ruta.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {ruta_csv}"
            )

        df = pd.read_csv(ruta)

        columnas_faltantes = [
            columna
            for columna in LectorCSV.COLUMNAS_OBLIGATORIAS
            if columna not in df.columns
        ]

        if columnas_faltantes:
            raise ValueError(
                f"Faltan columnas en el CSV: {columnas_faltantes}"
            )

        estudiantes = []

        for _, fila in df.iterrows():

            estudiante = Estudiante(
                codigo=str(fila["codigo"]),
                nombre=fila["nombre"],
                carrera=fila["carrera"],
                ciclo=int(fila["ciclo"]),
                edad=int(fila["edad"]),
                genero=fila["genero"],
                nota1=float(fila["nota1"]),
                nota2=float(fila["nota2"]),
                nota3=float(fila["nota3"]),
                nota4=float(fila["nota4"]),
                asistencia=int(fila["asistencia"])
            )

            estudiantes.append(estudiante)

        return estudiantes