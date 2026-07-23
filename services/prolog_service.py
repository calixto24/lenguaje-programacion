from pyswip import Prolog

from models.estudiante import Estudiante


class PrologService:

    def __init__(self):

        self.prolog = Prolog()
        self.prolog.consult("logic/reglas.pl")

    def cargar_estudiantes(self, estudiantes: list[Estudiante]):

        list(
            self.prolog.query(
                "retractall(estudiante(_,_,_,_,_,_,_,_,_,_,_))"
            )
        )

        for estudiante in estudiantes:
            trabaja = "si" if estudiante.trabaja else "no"
            discapacidad = "si" if estudiante.discapacidad else "no"
            orfandad = "si" if estudiante.orfandad else "no"

            tipo_colegio = estudiante.tipo_colegio.lower().strip()
            zona = estudiante.zona.lower().strip()
            departamento = estudiante.departamento.lower().strip()

            nombre_escapado = estudiante.nombre.replace("'", "\\'")

            consulta = (
                f"assertz("
                f"estudiante("
                f"'{nombre_escapado}',"
                f"{estudiante.promedio},"
                f"{estudiante.asistencia},"
                f"{estudiante.ingreso_familiar},"
                f"{estudiante.dependientes},"
                f"'{trabaja}',"
                f"'{discapacidad}',"
                f"'{orfandad}',"
                f"'{tipo_colegio}',"
                f"'{zona}',"
                f"'{departamento}'"
                f"))"
            )

            list(self.prolog.query(consulta))

    def obtener_beca(self, nombre: str):
        nombre_escapado = nombre.replace("'", "\\'")
        consulta = f"tipo_beca('{nombre_escapado}', Tipo)"

        resultado = list(self.prolog.query(consulta))

        if resultado:
            return resultado[0]["Tipo"]

        return "No Elegible"

    def obtener_resultados(self, estudiantes: list[Estudiante]):
        resultados = []

        for estudiante in estudiantes:
            beca = self.obtener_beca(estudiante.nombre)

            resultados.append(
                {
                    "codigo": estudiante.codigo,
                    "nombre": estudiante.nombre,
                    "carrera": estudiante.carrera,
                    "promedio": estudiante.promedio,
                    "beca": beca,
                }
            )

        return resultados

    def obtener_beca_integral(self):

        return [
            fila["Nombre"]
            for fila in self.prolog.query(
                "tipo_beca(Nombre,'Beca Integral (100%)')"
            )
        ]

    def obtener_beca_apoyo_social(self):

        return [
            fila["Nombre"]
            for fila in self.prolog.query(
                "tipo_beca(Nombre,'Beca de Apoyo Social (80%)')"
            )
        ]

    def obtener_beca_parcial(self):

        return [
            fila["Nombre"]
            for fila in self.prolog.query(
                "tipo_beca(Nombre,'Beca Parcial (70%)')"
            )
        ]

    def obtener_beca_esfuerzo(self):

        return [
            fila["Nombre"]
            for fila in self.prolog.query(
                "tipo_beca(Nombre,'Beca por Esfuerzo Académico (60%)')"
            )
        ]

    def obtener_no_elegibles(self):

        return [
            fila["Nombre"]
            for fila in self.prolog.query(
                "tipo_beca(Nombre,'No Elegible')"
            )
        ]