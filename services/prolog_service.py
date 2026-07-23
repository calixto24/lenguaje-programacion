from pyswip import Prolog
from models.expediente import Expediente


class PrologService:

    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult("logic/reglas.pl")

    def cargar_expedientes(self, expedientes: list[Expediente]):
        # Se elimina la base previa con aridad 14
        list(
            self.prolog.query(
                "retractall(estudiante(_,_,_,_,_,_,_,_,_,_,_,_,_,_))"
            )
        )

        for expediente in expedientes:
            codigo = expediente.codigo.strip()
            nombre = expediente.nombre.replace("'", "\\'")

            distrito = (
                expediente.distrito.lower().strip().replace(" ", "_")
            )

            trabaja = "si" if expediente.trabaja else "no"
            vive_solo = "si" if expediente.vive_solo else "no"
            discapacidad = "si" if expediente.discapacidad else "no"
            orfandad = "si" if expediente.orfandad else "no"
            recibe_otra_beca = (
                "si" if expediente.recibe_otra_beca else "no"
            )

            consulta = (
                f"assertz("
                f"estudiante("
                f"'{codigo}',"
                f"'{nombre}',"
                f"{expediente.promedio},"
                f"{expediente.asistencia},"
                f"{expediente.creditos},"
                f"'{distrito}',"
                f"{expediente.ingreso_familiar},"
                f"{expediente.dependientes},"
                f"'{trabaja}',"
                f"{expediente.horas_trabajo},"
                f"'{vive_solo}',"
                f"'{discapacidad}',"
                f"'{orfandad}',"
                f"'{recibe_otra_beca}'"
                f"))"
            )

            list(self.prolog.query(consulta))

    def obtener_beca(self, codigo: str):
        codigo_escapado = codigo.strip()
        consulta = f"tipo_beca('{codigo_escapado}', Tipo)"

        resultado = list(self.prolog.query(consulta))

        if resultado:
            return resultado[0]["Tipo"]

        return "No Elegible"

    def obtener_resultados(self, expedientes: list[Expediente]):
        resultados = []

        for expediente in expedientes:
            resultados.append(
                {
                    "codigo": expediente.codigo,
                    "nombre": expediente.nombre,
                    "carrera": expediente.carrera,
                    "promedio": expediente.promedio,
                    "beca": self.obtener_beca(expediente.codigo),
                }
            )

        return resultados

    # CONSULTAS ESPECÍFICAS
    def obtener_beca_socioeconomica(self):
        return [
            fila["Codigo"]
            for fila in self.prolog.query(
                "tipo_beca(Codigo,'Beca Socioeconómica (70%)')"
            )
        ]

    def obtener_beca_inclusion(self):
        return [
            fila["Codigo"]
            for fila in self.prolog.query(
                "tipo_beca(Codigo,'Beca de Inclusión (40%)')"
            )
        ]

    def obtener_beca_esfuerzo(self):
        return [
            fila["Codigo"]
            for fila in self.prolog.query(
                "tipo_beca(Codigo,'Beca por Esfuerzo Académico (20%)')"
            )
        ]

    def obtener_no_elegibles(self):
        return [
            fila["Codigo"]
            for fila in self.prolog.query(
                "tipo_beca(Codigo,'No Elegible')"
            )
        ]