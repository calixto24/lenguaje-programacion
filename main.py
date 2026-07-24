from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from services.lector_csv import LectorCSV
from services.expediente_service import ExpedienteService
from services.prolog_service import PrologService
from services.analisis_service import AnalisisService

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    estudiantes = LectorCSV.leer_estudiantes("data/estudiantes_utp.csv")
    postulaciones = LectorCSV.leer_postulaciones("data/postulaciones.csv")
    expedientes = ExpedienteService.generar_expedientes(estudiantes, postulaciones)

    prolog = PrologService()
    prolog.cargar_expedientes(expedientes)

    # Informacion de los estudiantes postulados
    resultados = prolog.obtener_resultados(expedientes)

    # Obtener métricas
    metricas = AnalisisService.calcular_metricas_generales(
        estudiantes, expedientes, resultados
    )

    # Obtener distribucion de becas
    distribucion = AnalisisService.obtener_distribucion_becas(resultados)

    # Obtener distribucion por distrito
    distribucion_distritos = AnalisisService.obtener_distribucion_por_distrito(expedientes, resultados)

    # Obtener estadistica ingreso por distrito
    ingresos_distrito = AnalisisService.obtener_ingreso_promedio_por_distrito(expedientes)

    contexto = {
        "titulo": "Evaluación del Sistema Experto de Becas",
        "resultados": resultados,
        "metricas": metricas,
        "distribucion": distribucion,
        "distribucion_distritos": distribucion_distritos,
        "ingresos_distrito": ingresos_distrito
    }

    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context=contexto,
    )