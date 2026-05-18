from datetime import datetime, timedelta
from collections import defaultdict

class Estadisticas:
    @staticmethod
    def total_por_materia(actividades):
        totales = defaultdict(int)
        for act in actividades:
            totales[act.materia] += act.duracion
        return totales

    @staticmethod
    def tendencia(actividades):
        if not actividades:
            return "Sin datos suficientes."

        hoy = datetime.now()
        semana_actual = hoy - timedelta(days=7)
        semana_anterior = hoy - timedelta(days=14)

        actual = sum(a.duracion for a in actividades if a.fecha >= semana_actual)
        anterior = sum(a.duracion for a in actividades if semana_anterior <= a.fecha < semana_actual)

        if actual > anterior:
            return "Tendencia positiva"
        if actual < anterior:
            return "Tendencia negativa"
        return "Tendencia estable"

