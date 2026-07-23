from pathlib import Path
import pandas as pd
from models.estudiante import Estudiante

class LectorCSV:

    COLUMNAS_OBLIGATORIAS = [
        "codigo",
        "nombre",
        "sexo",
        "edad",
        "carrera",
        "ciclo",
        "promedio",
        "asistencia",
        "ingreso_familiar",
        "dependientes",
        "trabaja",
        "tipo_colegio",
        "discapacidad",
        "orfandad",
        "departamento",
        "provincia",
        "zona"
    ]

    @staticmethod
    def texto_a_bool(valor: str) -> bool:
        return str(valor).strip().lower() == "si"

    @staticmethod
    def leer_estudiantes(ruta_csv: str) -> list[Estudiante]:

        ruta = Path(ruta_csv)

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
                sexo=fila["sexo"],
                edad=int(fila["edad"]),

                carrera=fila["carrera"],
                ciclo=int(fila["ciclo"]),
                promedio=float(fila["promedio"]),
                asistencia=int(fila["asistencia"]),

                ingreso_familiar=float(fila["ingreso_familiar"]),
                dependientes=int(fila["dependientes"]),
                trabaja=LectorCSV.texto_a_bool(fila["trabaja"]),

                tipo_colegio=fila["tipo_colegio"],
                discapacidad=LectorCSV.texto_a_bool(fila["discapacidad"]),
                orfandad=LectorCSV.texto_a_bool(fila["orfandad"]),

                departamento=fila["departamento"],
                provincia=fila["provincia"],
                zona=fila["zona"]
            )

            estudiantes.append(estudiante)

        return estudiantes