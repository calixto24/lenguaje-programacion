from pyswip import Prolog

from models.estudiante import Estudiante

class PrologService:

    def __init__(self):

        self.prolog = Prolog()
        self.prolog.consult("logic/reglas.pl")

    def cargar_estudiantes(self, estudiantes: list[Estudiante]):

        # Limpiar hechos anteriores
        list(self.prolog.query(
            "retractall(estudiante(_,_,_))"
        ))

        # Insertar nuevamente
        for estudiante in estudiantes:

            consulta = (
                f"assertz("
                f"estudiante("
                f"'{estudiante.nombre}',"
                f"{estudiante.promedio},"
                f"{estudiante.asistencia}"
                f"))"
            )

            list(self.prolog.query(consulta))

    def obtener_aprobados(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query("aprobado(Nombre)")
        ]

    def obtener_desaprobados(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query("desaprobado(Nombre)")
        ]

    def obtener_destacados(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query("destacado(Nombre)")
        ]

    def obtener_becarios(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query(
                "candidato_beca(Nombre)"
            )
        ]

    def obtener_tutoria(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query(
                "requiere_tutoria(Nombre)"
            )
        ]

    def obtener_riesgo_desercion(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query(
                "riesgo_desercion(Nombre)"
            )
        ]

    def obtener_asistencia_critica(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query(
                "asistencia_critica(Nombre)"
            )
        ]

    def obtener_rendimiento_regular(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query(
                "rendimiento_regular(Nombre)"
            )
        ]

    def obtener_buen_rendimiento(self):

        return [
            resultado["Nombre"]
            for resultado in
            self.prolog.query(
                "buen_rendimiento(Nombre)"
            )
        ]