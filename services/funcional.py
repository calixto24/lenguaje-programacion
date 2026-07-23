from functools import reduce

from models.estudiante import Estudiante


class FuncionalAcademico:

    # MAP
    @staticmethod
    def obtener_nombres(estudiantes: list[Estudiante]) -> list[str]:
        return list(map(lambda e: e.nombre, estudiantes))

    @staticmethod
    def obtener_promedios(estudiantes: list[Estudiante]) -> list[float]:
        return list(map(lambda e: e.promedio, estudiantes))

    @staticmethod
    def obtener_ingresos(estudiantes: list[Estudiante]) -> list[float]:
        return list(map(lambda e: e.ingreso_familiar, estudiantes))

    @staticmethod
    def obtener_carreras(estudiantes: list[Estudiante]) -> list[str]:
        return list(map(lambda e: e.carrera, estudiantes))

    @staticmethod
    def obtener_departamentos(estudiantes: list[Estudiante]) -> list[str]:
        return list(map(lambda e: e.departamento, estudiantes))

    @staticmethod
    def obtener_dependientes(estudiantes: list[Estudiante]) -> list[int]:
        return list(map(lambda e: e.dependientes, estudiantes))

    # FILTER
    @staticmethod
    def estudiantes_por_carrera(
        estudiantes: list[Estudiante],
        carrera: str
    ) -> list[Estudiante]:

        return list(
            filter(
                lambda e: e.carrera.lower() == carrera.lower(),
                estudiantes
            )
        )

    @staticmethod
    def estudiantes_por_departamento(
        estudiantes: list[Estudiante],
        departamento: str
    ) -> list[Estudiante]:

        return list(
            filter(
                lambda e: e.departamento.lower() == departamento.lower(),
                estudiantes
            )
        )

    @staticmethod
    def estudiantes_que_trabajan(
        estudiantes: list[Estudiante]
    ) -> list[Estudiante]:

        return list(
            filter(
                lambda e: e.trabaja,
                estudiantes
            )
        )

    @staticmethod
    def estudiantes_con_discapacidad(
        estudiantes: list[Estudiante]
    ) -> list[Estudiante]:

        return list(
            filter(
                lambda e: e.discapacidad,
                estudiantes
            )
        )

    @staticmethod
    def estudiantes_huerfanos(
        estudiantes: list[Estudiante]
    ) -> list[Estudiante]:

        return list(
            filter(
                lambda e: e.orfandad,
                estudiantes
            )
        )

    @staticmethod
    def estudiantes_colegio_publico(
        estudiantes: list[Estudiante]
    ) -> list[Estudiante]:

        return list(
            filter(
                lambda e: e.tipo_colegio.lower() == "publico",
                estudiantes
            )
        )

    @staticmethod
    def estudiantes_zona_rural(
        estudiantes: list[Estudiante]
    ) -> list[Estudiante]:

        return list(
            filter(
                lambda e: e.zona.lower() == "rural",
                estudiantes
            )
        )

    # REDUCE
    @staticmethod
    def cantidad_estudiantes(
        estudiantes: list[Estudiante]
    ) -> int:

        return reduce(
            lambda total, _: total + 1,
            estudiantes,
            0
        )

    @staticmethod
    def suma_promedios(
        estudiantes: list[Estudiante]
    ) -> float:

        return reduce(
            lambda total, e: total + e.promedio,
            estudiantes,
            0.0
        )

    @staticmethod
    def suma_ingresos(
        estudiantes: list[Estudiante]
    ) -> float:

        return reduce(
            lambda total, e: total + e.ingreso_familiar,
            estudiantes,
            0.0
        )

    @staticmethod
    def total_dependientes(
        estudiantes: list[Estudiante]
    ) -> int:

        return reduce(
            lambda total, e: total + e.dependientes,
            estudiantes,
            0
        )

    @staticmethod
    def promedio_general(
        estudiantes: list[Estudiante]
    ) -> float:

        total = FuncionalAcademico.cantidad_estudiantes(estudiantes)

        if total == 0:
            return 0.0

        return round(
            FuncionalAcademico.suma_promedios(estudiantes) / total,
            2
        )

    @staticmethod
    def ingreso_promedio(
        estudiantes: list[Estudiante]
    ) -> float:

        total = FuncionalAcademico.cantidad_estudiantes(estudiantes)

        if total == 0:
            return 0.0

        return round(
            FuncionalAcademico.suma_ingresos(estudiantes) / total,
            2
        )