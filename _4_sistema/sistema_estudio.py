from datetime import datetime, timedelta
from _2_modelo.usuario import Usuario
from _2_modelo.materia import Materia
from _2_modelo.actividad import ActividadEstudio
from _3_inteligencia.estadisticas import Estadisticas
from _3_inteligencia.control_objetivos import ControlObjetivos
from _3_inteligencia.recomendaciones import Recomendaciones
from _3_inteligencia.analizador_semanal import AnalizadorSemanal
from _3_inteligencia.gestor_alertas import GestorAlertas
from _1_excepciones.errores import *

class SistemaEstudio:
    def __init__(self):
        self.usuarios = {}

    def _get_user(self, correo):
        if correo not in self.usuarios:
            raise UsuarioNoEncontradoError("Usuario no encontrado.")
        return self.usuarios[correo]

    def registrar_usuario(self, nombre, correo):
        if correo in self.usuarios:
            raise UsuarioDuplicadoError("El correo ya existe.")
        self.usuarios[correo] = Usuario(nombre, correo)

    def registrar_materia(self, correo, materia):
        u = self._get_user(correo)
        if materia in u.materias:
            raise DatoInvalidoError("La materia ya existe.")
        u.materias[materia] = Materia(materia)

    def registrar_actividad(self, correo, materia, duracion):
        u = self._get_user(correo)
        if materia not in u.materias:
            raise MateriaNoEncontradaError("La materia no existe.")
        u.actividades.append(ActividadEstudio(datetime.now(), materia, duracion))

    def historial(self, correo):
        return self._get_user(correo).obtener_actividades()

    def estadisticas(self, correo, periodo):
        u = self._get_user(correo)
        acts = u.obtener_actividades()
        limite = datetime.now() - timedelta(days=7 if periodo == "semana" else 30)
        filtradas = [a for a in acts if a.fecha >= limite]
        return Estadisticas.total_por_materia(filtradas), Estadisticas.tendencia(acts)

    def definir_meta(self, correo, materia, horas):
        self._get_user(correo).metas[materia] = horas

    def verificar_metas(self, correo):
        u = self._get_user(correo)
        tiempos = Estadisticas.total_por_materia(u.actividades)
        return {m: ControlObjetivos.verificar(meta, tiempos.get(m, 0)) for m, meta in u.metas.items()}

    def recomendaciones(self, correo):
        u = self._get_user(correo)
        tiempos = Estadisticas.total_por_materia(u.actividades)
        return Recomendaciones.generar(tiempos, u.metas)

    def inactividad(self, correo, umbral):
        u = self._get_user(correo)
        acts = u.obtener_actividades()
        if not acts:
            return None, "No hay actividades."
        dias = (datetime.now() - acts[-1].fecha).days
        return dias, ("Falta de constancia" if dias >= umbral else "Constancia aceptable")

    def analisis_semanal(self, correo):
        return AnalizadorSemanal.evaluar(self._get_user(correo).actividades)

    def alertas(self, correo, umbral):
        u = self._get_user(correo)
        tiempos = Estadisticas.total_por_materia(u.actividades)
        acts = u.obtener_actividades()
        dias = (datetime.now() - acts[-1].fecha).days if acts else None
        return GestorAlertas.generar(tiempos, u.metas, dias)
