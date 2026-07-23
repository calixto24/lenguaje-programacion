from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    students = {
        "titulo": "Resultado de Evaluación de Beca",
        "estudiante_nombre": "Carlos Mendoza",
        "promedio": 17.5,
        "porcentaje_beca": 100,
        "observacion": "Aprobado por excelente rendimiento y vulnerabilidad alta."
    }

    return templates.TemplateResponse(
        request=request,
        name='index.html',
        context=students,
    )
