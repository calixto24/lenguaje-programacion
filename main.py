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
    resultados = prolog.obtener_resultados(expedientes)

    # Obtener métricas
    metricas = AnalisisService.calcular_metricas_generales(
        expedientes, resultados
    )

    contexto = {
        "titulo": "Evaluación del Sistema Experto de Becas",
        "resultados": resultados,
        "metricas": metricas
    }

    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context=contexto,
    )