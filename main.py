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

    # Mostrar estudiantes
    print("=" * 60)
    print("LISTA DE ESTUDIANTES")
    print("=" * 60)

    for estudiante in estudiantes:
        print(estudiante)

    # ANÁLISIS CON PANDAS Y NUMPY
    analizador = AnalizadorAcademico(estudiantes)

    print("\n")
    print("=" * 60)
    print("ESTADÍSTICAS")
    print("=" * 60)

    resumen = analizador.resumen()

    for clave, valor in resumen.items():
        print(f"{clave}: {valor}")

    print("\n")

    print("Promedio por carrera")

    print(
        analizador.promedio_por_carrera()
    )

    print("\n")

    print("Promedio por ciclo")

    print(
        analizador.promedio_por_ciclo()
    )

    # PROLOG
    print("\n")
    print("=" * 60)
    print("PROLOG")
    print("=" * 60)

    prolog = PrologService()

    prolog.cargar_estudiantes(estudiantes)

    print("\nEstudiantes destacados")

    print(
        prolog.obtener_destacados()
    )

    print("\nCandidatos a beca")

    print(
        prolog.obtener_becarios()
    )

    print("\nRequieren tutoría")

    print(
        prolog.obtener_tutoria()
    )

    print("\nRiesgo de deserción")

    print(
        prolog.obtener_riesgo_desercion()
    )

    print("\nAsistencia crítica")

    print(
        prolog.obtener_asistencia_critica()
    )

    print("\nBuen rendimiento")

    print(
        prolog.obtener_buen_rendimiento()
    )

    print("\nRendimiento regular")

    print(
        prolog.obtener_rendimiento_regular()
    )


if __name__ == "__main__":
    main()