from models.estudiante import Estudiante
from models.postulacion import Postulacion
from models.expediente import Expediente

class ExpedienteService:

    @staticmethod
    def generar_expedientes(
        estudiantes: list[Estudiante],
        postulaciones: list[Postulacion]
    ) -> list[Expediente]:
        # Diccionario para búsqueda rápida 
        estudiantes_dict = {
            estudiante.codigo: estudiante
            for estudiante in estudiantes
        }

        expedientes = []

        for postulacion in postulaciones:

            estudiante = estudiantes_dict.get(
                postulacion.codigo
            )

            if estudiante is None:
                print(
                    f"[ADVERTENCIA] "
                    f"No existe el estudiante "
                    f"{postulacion.codigo}"
                )
                continue

            expediente = Expediente(
                estudiante=estudiante,
                postulacion=postulacion
            )

            expedientes.append(expediente)

        return expedientes