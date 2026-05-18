class GestorAlertas:
    @staticmethod
    def generar(tiempos, metas, dias_sin):
        alertas = []
        for materia, meta in metas.items():
            real = tiempos.get(materia, 0) / 60
            if real < meta * 0.5:
                alertas.append(f"⚠ Muy poco tiempo dedicado a {materia}.")
        if dias_sin is not None and dias_sin >= 5:
            alertas.append(f"⚠ Llevas {dias_sin} días sin estudiar.")
        return alertas or ["No se detectan alertas de bajo rendimiento."]
