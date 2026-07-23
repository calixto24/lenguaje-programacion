from pathlib import Path
import pandas as pd

from models.estudiante import Estudiante
from models.postulacion import Postulacion

class LectorCSV:

    COLUMNAS_ESTUDIANTES = [
        "codigo",
        "nombre",
        "carrera",
        "ciclo",
        "creditos_matriculados",
        "promedio_ciclo_anterior",
        "asistencia",
        "distrito",
        "edad",
        "sexo"
    ]

    COLUMNAS_POSTULACIONES = [
        "codigo",
        "ingreso_familiar",
        "dependientes",
        "trabaja",
        "horas_trabajo",
        "vive_solo",
        "discapacidad",
        "orfandad",
        "recibe_otra_beca"
    ]

    @staticmethod
    def texto_a_bool(valor):
        return (
            str(valor)
            .strip()
            .lower()
            == "si"
        )

    @staticmethod
    def validar_columnas(df, columnas):
        faltantes = [
            columna
            for columna in columnas
            if columna not in df.columns
        ]

        if faltantes:
            raise ValueError(
                f"Faltan columnas en CSV: {faltantes}"
            )

    @staticmethod
    def leer_estudiantes(
            ruta_csv: str
    ) -> list[Estudiante]:
        ruta = Path(ruta_csv)

        if not ruta.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {ruta_csv}"
            )
        df = pd.read_csv(ruta)

        LectorCSV.validar_columnas(
            df,
            LectorCSV.COLUMNAS_ESTUDIANTES
        )

        estudiantes = []


        for _, fila in df.iterrows():

            estudiante = Estudiante(

                codigo=str(
                    fila["codigo"]
                ),
                nombre=fila["nombre"],
                carrera=fila["carrera"],
                ciclo=int(
                    fila["ciclo"]
                ),
                creditos_matriculados=int(
                    fila["creditos_matriculados"]
                ),
                promedio_ciclo_anterior=float(
                    fila["promedio_ciclo_anterior"]
                ),
                asistencia=float(
                    fila["asistencia"]
                ),
                distrito=fila["distrito"],
                edad=int(
                    fila["edad"]
                ),
                sexo=fila["sexo"]
            )
            estudiantes.append(estudiante)
        return estudiantes

    @staticmethod
    def leer_postulaciones(
            ruta_csv: str
    ) -> list[Postulacion]:

        ruta = Path(ruta_csv)

        if not ruta.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {ruta_csv}"
            )

        df = pd.read_csv(ruta)

        LectorCSV.validar_columnas(
            df,
            LectorCSV.COLUMNAS_POSTULACIONES
        )

        postulaciones = []

        for _, fila in df.iterrows():
            postulacion = Postulacion(

                codigo=str(
                    fila["codigo"]
                ),
                ingreso_familiar=float(
                    fila["ingreso_familiar"]
                ),
                dependientes=int(
                    fila["dependientes"]
                ),
                trabaja=LectorCSV.texto_a_bool(
                    fila["trabaja"]
                ),
                horas_trabajo=int(
                    fila["horas_trabajo"]
                ),
                vive_solo=LectorCSV.texto_a_bool(
                    fila["vive_solo"]
                ),
                discapacidad=LectorCSV.texto_a_bool(
                    fila["discapacidad"]
                ),
                orfandad=LectorCSV.texto_a_bool(
                    fila["orfandad"]
                ),
                recibe_otra_beca=LectorCSV.texto_a_bool(
                    fila["recibe_otra_beca"]
                )
            )
            postulaciones.append(postulacion)
        return postulaciones