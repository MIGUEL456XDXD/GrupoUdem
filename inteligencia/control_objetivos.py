from excepciones.errores import DatoInvalidoError

class ControlObjetivos:
    @staticmethod
    def verificar(meta_horas, minutos_reales):
        if meta_horas <= 0:
            raise DatoInvalidoError("La meta debe ser mayor a 0.")
        horas = minutos_reales / 60
        porcentaje = (horas / meta_horas) * 100
        if porcentaje >= 100: return porcentaje, "Meta cumplida"
        if porcentaje >= 70: return porcentaje, "En buen camino"
        return porcentaje, "En riesgo"
