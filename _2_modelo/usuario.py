class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.materias = {}
        self.actividades = []
        self.metas = {}

    def obtener_actividades(self):
        return sorted(self.actividades, key=lambda a: a.fecha)
