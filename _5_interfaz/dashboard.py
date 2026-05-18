import tkinter as tk
from tkinter import messagebox

class Dashboard(tk.Tk):
    def __init__(self, sistema):
        super().__init__()
        self.sistema = sistema
        self.title("Sistema Inteligente de Hábitos de Estudio")
        self.geometry("900x700")
        self.configure(bg="#f0f0f0")
        self._crear_ui()

    def _crear_ui(self):
        tk.Label(self, text="SISTEMA INTELIGENTE DE HÁBITOS DE ESTUDIO",
                 font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Label(self, text="DASHBOARD PRINCIPAL",
                 font=("Arial", 14), bg="#f0f0f0").pack(pady=5)


        frame1 = tk.LabelFrame(self, text="GESTIÓN BÁSICA",
                               font=("Arial", 12, "bold"), padx=20, pady=20)
        frame1.pack(fill="x", padx=20, pady=10)

        self._boton(frame1, "Registrar Usuario", self.ui_registrar_usuario)
        self._boton(frame1, "Registrar Materia", self.ui_registrar_materia)
        self._boton(frame1, "Registrar Actividad", self.ui_registrar_actividad)
        self._boton(frame1, "Consultar Historial", self.ui_historial)


        frame2 = tk.LabelFrame(self, text="FUNCIONES INTELIGENTES ★",
                               font=("Arial", 12, "bold"), padx=20, pady=20)
        frame2.pack(fill="x", padx=20, pady=10)

        self._boton(frame2, "Generar Estadísticas ★", self.ui_estadisticas)
        self._boton(frame2, "Verificar Objetivos ★", self.ui_objetivos)
        self._boton(frame2, "Recomendaciones Automáticas ★", self.ui_recomendaciones)
        self._boton(frame2, "Detectar Inactividad ★", self.ui_inactividad)
        self._boton(frame2, "Análisis Semanal ★", self.ui_analisis)
        self._boton(frame2, "Alertas de Rendimiento ★", self.ui_alertas)

        # Panel de resultados (SOLO LECTURA)
        frame3 = tk.LabelFrame(self, text="PANEL DE RESULTADOS",
                               font=("Arial", 12, "bold"), padx=20, pady=20)
        frame3.pack(fill="both", expand=True, padx=20, pady=10)

        self.panel = tk.Text(frame3, font=("Arial", 11), state="disabled")
        self.panel.pack(fill="both", expand=True)

        # Botón salir
        tk.Button(self, text="SALIR", font=("Arial", 12, "bold"),
                  bg="#d9534f", fg="white", width=12,
                  command=self.destroy).pack(pady=10)

    def _boton(self, frame, texto, comando):
        tk.Button(frame, text=texto, font=("Arial", 11),
                  width=25, command=comando).pack(pady=5)



    def limpiar(self):
        self.panel.config(state="normal")
        self.panel.delete("1.0", tk.END)
        self.panel.config(state="disabled")

    def escribir(self, texto):
        self.panel.config(state="normal")
        self.panel.insert(tk.END, texto)
        self.panel.config(state="disabled")


    def ui_registrar_usuario(self):
        win = tk.Toplevel(self)
        win.title("Registrar Usuario")

        tk.Label(win, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Correo:").grid(row=1, column=0, padx=5, pady=5)
        e2 = tk.Entry(win); e2.grid(row=1, column=1, padx=5, pady=5)

        def registrar():
            try:
                self.sistema.registrar_usuario(e1.get().strip(), e2.get().strip())
                self.limpiar()
                self.escribir(f"Usuario registrado: {e1.get()} ({e2.get()})\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Registrar", command=registrar).grid(row=2, column=0, columnspan=2, pady=10)


    def ui_registrar_materia(self):
        win = tk.Toplevel(self)
        win.title("Registrar Materia")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Materia:").grid(row=1, column=0, padx=5, pady=5)
        e2 = tk.Entry(win); e2.grid(row=1, column=1, padx=5, pady=5)

        def registrar():
            try:
                self.sistema.registrar_materia(e1.get().strip(), e2.get().strip())
                self.limpiar()
                self.escribir(f"Materia registrada: {e2.get()} para {e1.get()}\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Registrar", command=registrar).grid(row=2, column=0, columnspan=2, pady=10)


    def ui_registrar_actividad(self):
        win = tk.Toplevel(self)
        win.title("Registrar Actividad")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Materia:").grid(row=1, column=0, padx=5, pady=5)
        e2 = tk.Entry(win); e2.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(win, text="Duración (min):").grid(row=2, column=0, padx=5, pady=5)
        e3 = tk.Entry(win); e3.grid(row=2, column=1, padx=5, pady=5)

        def registrar():
            try:
                dur = int(e3.get().strip())
                self.sistema.registrar_actividad(e1.get().strip(), e2.get().strip(), dur)
                self.limpiar()
                self.escribir(f"Actividad: {e2.get()} - {dur} min\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Registrar", command=registrar).grid(row=3, column=0, columnspan=2, pady=10)


    def ui_historial(self):
        win = tk.Toplevel(self)
        win.title("Consultar Historial")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        def consultar():
            try:
                acts = self.sistema.historial(e1.get().strip())
                self.limpiar()
                if not acts:
                    self.escribir("No hay actividades registradas.\n")
                else:
                    for a in acts:
                        self.escribir(
                            f"{a.fecha.strftime('%Y-%m-%d %H:%M')} | {a.materia} | {a.duracion} min\n"
                        )
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Consultar", command=consultar).grid(row=1, column=0, columnspan=2, pady=10)


    def ui_estadisticas(self):
        win = tk.Toplevel(self)
        win.title("Generar Estadísticas")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Periodo (semana/mes):").grid(row=1, column=0, padx=5, pady=5)
        e2 = tk.Entry(win); e2.insert(0, "semana"); e2.grid(row=1, column=1, padx=5, pady=5)

        def generar():
            try:
                periodo = e2.get().strip().lower()
                if periodo not in ("semana", "mes"):
                    periodo = "semana"
                tot, tend = self.sistema.estadisticas(e1.get().strip(), periodo)
                self.limpiar()
                self.escribir(f"Estadísticas ({periodo}):\n\n")
                if not tot:
                    self.escribir("No hay actividades en el periodo.\n")
                else:
                    for m, t in tot.items():
                        self.escribir(f"{m}: {t} min ({t/60:.2f} h)\n")
                self.escribir(f"\nTendencia: {tend}\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Generar", command=generar).grid(row=2, column=0, columnspan=2, pady=10)


    def ui_objetivos(self):
        win = tk.Toplevel(self)
        win.title("Control de Objetivos")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Materia:").grid(row=1, column=0, padx=5, pady=5)
        e2 = tk.Entry(win); e2.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(win, text="Meta (horas):").grid(row=2, column=0, padx=5, pady=5)
        e3 = tk.Entry(win); e3.grid(row=2, column=1, padx=5, pady=5)

        def definir():
            try:
                meta = float(e3.get().strip())
                self.sistema.definir_meta(e1.get().strip(), e2.get().strip(), meta)
                messagebox.showinfo("Éxito", "Meta definida correctamente.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        def verificar():
            try:
                res = self.sistema.verificar_metas(e1.get().strip())
                self.limpiar()
                if not res:
                    self.escribir("No hay metas definidas.\n")
                else:
                    for m, (p, est) in res.items():
                        self.escribir(f"{m}: {p:.1f}% - {est}\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Definir meta", command=definir).grid(row=3, column=0, pady=10)
        tk.Button(win, text="Verificar metas", command=verificar).grid(row=3, column=1, pady=10)


    def ui_recomendaciones(self):
        win = tk.Toplevel(self)
        win.title("Recomendaciones Automáticas")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        def ver():
            try:
                recs = self.sistema.recomendaciones(e1.get().strip())
                self.limpiar()
                self.escribir("Recomendaciones:\n\n")
                for r in recs:
                    self.escribir(f"- {r}\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Ver recomendaciones", command=ver).grid(row=1, column=0, columnspan=2, pady=10)

    def ui_inactividad(self):
        win = tk.Toplevel(self)
        win.title("Detección de Inactividad")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Umbral (días):").grid(row=1, column=0, padx=5, pady=5)
        e2 = tk.Entry(win); e2.insert(0, "5"); e2.grid(row=1, column=1, padx=5, pady=5)

        def detectar():
            try:
                umbral = int(e2.get().strip())
                dias, estado = self.sistema.inactividad(e1.get().strip(), umbral)
                self.limpiar()
                if dias is None:
                    self.escribir("No hay actividades registradas.\n")
                else:
                    self.escribir(f"Días sin actividad: {dias}\nEstado: {estado}\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Detectar inactividad", command=detectar).grid(row=2, column=0, columnspan=2, pady=10)


    def ui_analisis(self):
        win = tk.Toplevel(self)
        win.title("Análisis Semanal")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        def analizar():
            try:
                horas, nivel = self.sistema.analisis_semanal(e1.get().strip())
                self.limpiar()
                self.escribir(f"Horas de estudio (última semana): {horas:.2f}\n")
                self.escribir(f"Nivel de rendimiento: {nivel}\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Analizar semana", command=analizar).grid(row=1, column=0, columnspan=2, pady=10)


    def ui_alertas(self):
        win = tk.Toplevel(self)
        win.title("Alertas de Rendimiento")

        tk.Label(win, text="Correo:").grid(row=0, column=0, padx=5, pady=5)
        e1 = tk.Entry(win); e1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Umbral inactividad (días):").grid(row=1, column=0, padx=5, pady=5)
        e2 = tk.Entry(win); e2.insert(0, "5"); e2.grid(row=1, column=1, padx=5, pady=5)

        def generar():
            try:
                umbral = int(e2.get().strip())
                alertas = self.sistema.alertas(e1.get().strip(), umbral)
                self.limpiar()
                self.escribir("Alertas de rendimiento:\n\n")
                for a in alertas:
                    self.escribir(f"- {a}\n")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(win, text="Generar alertas", command=generar).grid(row=2, column=0, columnspan=2, pady=10)