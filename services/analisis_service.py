import numpy as np
from models.expediente import Expediente
from services.funcional_service import FuncionalService

class AnalisisService:

    @staticmethod
    def calcular_metricas_generales(estudiantes: list[Estudiante], expedientes: list[Expediente], resultados_prolog: list[dict]) -> dict:
        # Asociación de cada expediente con el resultado obtenido en Prolog
        beca_map = {r["codigo"]: r["beca"] for r in resultados_prolog}
        expedientes_con_beca = [(exp, beca_map.get(exp.codigo, "No Elegible")) for exp in expedientes]

        # Aplicando programación funcional para segmentar datos
        beneficiarios = FuncionalService.filtrar_beneficiarios(expedientes_con_beca)
        
        ingresos_todos = np.array(FuncionalService.extraer_ingresos(expedientes))
        promedios_todos = np.array(FuncionalService.extraer_promedios(expedientes))

        ingresos_beneficiarios = np.array(
            FuncionalService.extraer_ingresos(list(map(lambda t: t[0], beneficiarios)))
        ) if beneficiarios else np.array([0.0])

        return {
            "total_bd": len(estudiantes),
            "total_estudiantes": len(expedientes),
            "total_becas_aprobadas": len(beneficiarios),
            "tasa_aprobacion_pct": round((len(beneficiarios) / len(expedientes)) * 100, 2) if expedientes else 0.0,
            "promedio_ingreso_general": round(float(np.mean(ingresos_todos)), 2),
            "mediana_ingreso_general": round(float(np.median(ingresos_todos)), 2),
            "promedio_ingreso_beneficiarios": round(float(np.mean(ingresos_beneficiarios)), 2),
            "promedio_academico_general": round(float(np.mean(promedios_todos)), 2),
            "desviacion_promedio_academico": round(float(np.std(promedios_todos)), 2)
        }

    @staticmethod
    def obtener_distribucion_becas(resultados_prolog):

        tipos = [r["beca"] for r in resultados_prolog]

        labels, valores = np.unique(
            tipos,
            return_counts=True
        )

        return {
            "labels": labels.tolist(),
            "series": valores.astype(int).tolist()
        }

    @staticmethod
    def obtener_distribucion_por_distrito(
        expedientes: list[Expediente],
        resultados_prolog: list[dict]
    ) -> dict:

        beca_map = {
            r["codigo"]: r["beca"]
            for r in resultados_prolog
        }

        distritos = np.array([
            exp.distrito.title().strip()
            for exp in expedientes
        ])

        beneficiarios = np.array([
            beca_map.get(exp.codigo, "No Elegible") != "No Elegible"
            for exp in expedientes
        ])

        distritos_unicos = np.unique(distritos)

        labels = []
        series = []

        for distrito in distritos_unicos:

            total = np.sum(distritos == distrito)

            aprobados = np.sum(
                (distritos == distrito) & beneficiarios
            )

            labels.append(distrito)
            series.append(int(aprobados))

        return {
            "labels": labels,
            "series": series
        }