from services.lector_csv import LectorCSV
from services.funcional import FuncionalAcademico
from services.analisis import AnalizadorBecas
from services.prolog_service import PrologService


def main():

    print("=" * 70)
    print(" SISTEMA EXPERTO PARA LA ASIGNACIÓN DE BECAS UNIVERSITARIAS ")
    print("=" * 70)

    # ======================================================
    # Leer CSV
    # ======================================================

    estudiantes = LectorCSV.leer_estudiantes(
        "data/estudiantes.csv"
    )

    print(f"\nSe cargaron {len(estudiantes)} estudiantes.")

    # ======================================================
    # PROGRAMACIÓN FUNCIONAL
    # ======================================================

    print("\n" + "=" * 70)
    print("PROGRAMACIÓN FUNCIONAL")
    print("=" * 70)

    print("\nPrimeros cinco nombres:")

    print(
        FuncionalAcademico.obtener_nombres(estudiantes)[:5]
    )

    print("\nPromedio general (Reduce):")

    print(
        FuncionalAcademico.promedio_general(estudiantes)
    )

    print("\nEstudiantes que trabajan:")

    trabajan = FuncionalAcademico.estudiantes_que_trabajan(
        estudiantes
    )

    for estudiante in trabajan[:5]:
        print("-", estudiante.nombre)

    # ======================================================
    # NUMPY Y PANDAS
    # ======================================================

    analizador = AnalizadorBecas(estudiantes)

    print("\n" + "=" * 70)
    print("ANÁLISIS ESTADÍSTICO")
    print("=" * 70)

    print(f"\nPromedio general: {analizador.promedio_general()}")

    print(f"Ingreso promedio: S/. {analizador.ingreso_promedio()}")

    print(
        f"Desviación de ingresos: {analizador.desviacion_ingresos()}"
    )

    print(
        f"Promedio de dependientes: {analizador.promedio_dependientes()}"
    )

    print("\nPromedio por carrera:")

    print(
        analizador.promedio_por_carrera()
    )

    print("\nCantidad por departamento:")

    print(
        analizador.estudiantes_por_departamento()
    )

    # ======================================================
    # PROLOG
    # ======================================================

    prolog = PrologService()

    prolog.cargar_estudiantes(estudiantes)

    print("\n" + "=" * 70)
    print("RESULTADO DEL SISTEMA EXPERTO")
    print("=" * 70)

    resultados = prolog.obtener_resultados(estudiantes)

    print(
        f"{'Código':<10}"
        f"{'Nombre':<25}"
        f"{'Promedio':<12}"
        f"{'Beca'}"
    )

    print("-" * 90)

    for r in resultados:
        print(
            f"{r['codigo']:<10}"
            f"{r['nombre']:<25}"
            f"{r['promedio']:<12}"
            f"{r['beca']}"
        )

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()