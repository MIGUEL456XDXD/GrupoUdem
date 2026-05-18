from datetime import datetime, timedelta

class AnalizadorSemanal:
    @staticmethod
    def evaluar(actividades):
        hoy = datetime.now()
        semana = hoy - timedelta(days=7)
        total = sum(a.duracion for a in actividades if a.fecha >= semana)
        horas = total / 60
        if horas >= 10: return horas, "Alto"
        if horas >= 5: return horas, "Medio"
        if horas > 0: return horas, "Bajo"
        return horas, "Sin actividad"
