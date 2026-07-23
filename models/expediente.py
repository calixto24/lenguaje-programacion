from dataclasses import dataclass

from models.estudiante import Estudiante
from models.postulacion import Postulacion

@dataclass
class Expediente:

    estudiante: Estudiante
    postulacion: Postulacion

    @property
    def codigo(self):
        return self.estudiante.codigo

    @property
    def nombre(self):
        return self.estudiante.nombre

    @property
    def carrera(self):
        return self.estudiante.carrera

    @property
    def ciclo(self):
        return self.estudiante.ciclo

    @property
    def creditos(self):
        return self.estudiante.creditos_matriculados

    @property
    def promedio(self):
        return self.estudiante.promedio_ciclo_anterior

    @property
    def asistencia(self):
        return self.estudiante.asistencia

    @property
    def distrito(self):
        return self.estudiante.distrito

    @property
    def edad(self):
        return self.estudiante.edad

    @property
    def sexo(self):
        return self.estudiante.sexo

    @property
    def ingreso_familiar(self):
        return self.postulacion.ingreso_familiar

    @property
    def dependientes(self):
        return self.postulacion.dependientes

    @property
    def trabaja(self):
        return self.postulacion.trabaja

    @property
    def horas_trabajo(self):
        return self.postulacion.horas_trabajo

    @property
    def vive_solo(self):
        return self.postulacion.vive_solo

    @property
    def discapacidad(self):
        return self.postulacion.discapacidad

    @property
    def orfandad(self):
        return self.postulacion.orfandad

    @property
    def recibe_otra_beca(self):
        return self.postulacion.recibe_otra_beca

    def to_dict(self):

        return {

            "codigo": self.codigo,
            "nombre": self.nombre,
            "carrera": self.carrera,
            "ciclo": self.ciclo,
            "creditos": self.creditos,
            "promedio": self.promedio,
            "asistencia": self.asistencia,
            "distrito": self.distrito,
            "edad": self.edad,
            "sexo": self.sexo,

            "ingreso_familiar": self.ingreso_familiar,
            "dependientes": self.dependientes,
            "trabaja": self.trabaja,
            "horas_trabajo": self.horas_trabajo,
            "vive_solo": self.vive_solo,
            "discapacidad": self.discapacidad,
            "orfandad": self.orfandad,
            "recibe_otra_beca": self.recibe_otra_beca
        }