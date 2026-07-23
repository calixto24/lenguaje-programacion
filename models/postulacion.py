from dataclasses import dataclass

@dataclass
class Postulacion:
    codigo: str
    ingreso_familiar: float
    dependientes: int
    trabaja: bool
    horas_trabajo: int
    vive_solo: bool
    discapacidad: bool
    orfandad: bool
    recibe_otra_beca: bool

    def to_dict(self):

        return {
            "codigo": self.codigo,
            "ingreso_familiar": self.ingreso_familiar,
            "dependientes": self.dependientes,
            "trabaja": self.trabaja,
            "horas_trabajo": self.horas_trabajo,
            "vive_solo": self.vive_solo,
            "discapacidad": self.discapacidad,
            "orfandad": self.orfandad,
            "recibe_otra_beca": self.recibe_otra_beca
        }