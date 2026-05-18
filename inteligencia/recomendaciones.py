class Recomendaciones:
    @staticmethod
    def generar(tiempos, metas):
        recs = []
        for materia, meta in metas.items():
            real_horas = tiempos.get(materia, 0) / 60
            if real_horas < meta:
                faltante = meta - real_horas
                recs.append(f"Dedica más tiempo a {materia}: faltan {faltante:.1f} horas.")
        return recs or ["Buen trabajo: no se detectan materias con déficit."]
