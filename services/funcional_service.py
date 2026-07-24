from functools import reduce
from models.expediente import Expediente


class FuncionalService:

    # --- CONSULTAS DE FILTRADO (filter) ---

    @staticmethod
    def filtrar_beneficiarios(expedientes_con_beca: list[tuple[Expediente, str]]) -> list[tuple[Expediente, str]]:
        return list(
            filter(
                lambda item: item[1] != "No Elegible",
                expedientes_con_beca
            )
        )

    @staticmethod
    def filtrar_no_elegibles(expedientes_con_beca: list[tuple[Expediente, str]]) -> list[tuple[Expediente, str]]:
        return list(
            filter(
                lambda item: item[1] == "No Elegible",
                expedientes_con_beca
            )
        )

    @staticmethod
    def filtrar_por_distrito(expedientes: list[Expediente], distrito: str) -> list[Expediente]:
        distrito_normalizado = distrito.lower().strip()
        return list(
            filter(
                lambda exp: exp.distrito.lower().strip() == distrito_normalizado,
                expedientes
            )
        )

    # --- TRANSFORMACIONES (map) ---

    @staticmethod
    def extraer_ingresos(expedientes: list[Expediente]) -> list[float]:
        return list(map(lambda exp: float(exp.ingreso_familiar), expedientes))

    @staticmethod
    def extraer_promedios(expedientes: list[Expediente]) -> list[float]:
        return list(map(lambda exp: float(exp.promedio), expedientes))

    @staticmethod
    def extraer_tipos_beca(expedientes_con_beca: list[tuple[Expediente, str]]) -> list[str]:
        return list(map(lambda item: item[1], expedientes_con_beca))

    # --- AGREGACIONES (reduce) ---

    @staticmethod
    def contar_total(expedientes: list) -> int:
        return reduce(lambda acc, _: acc + 1, expedientes, 0)

    @staticmethod
    def sumar_ingresos(expedientes: list[Expediente]) -> float:
        return reduce(
            lambda acc, exp: acc + exp.ingreso_familiar,
            expedientes,
            0.0
        )