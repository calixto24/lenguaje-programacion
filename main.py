from services.lector_csv import LectorCSV
from services.analisis import AnalizadorAcademico
from services.funcional import FuncionalAcademico
from services.prolog_service import PrologService


def main():

    print("=" * 60)
    print(" SISTEMA DE ANÁLISIS DE RENDIMIENTO ACADÉMICO ")
    print("=" * 60)

    # Leer CSV
    estudiantes = LectorCSV.leer_estudiantes(
        "data/estudiantes.csv"
    )

    print(f"\nSe cargaron {len(estudiantes)} estudiantes.\n")