from sistema.sistema_estudio import SistemaEstudio
from interfaz.dashboard import Dashboard

def main():
    sistema = SistemaEstudio()
    app = Dashboard(sistema)
    app.mainloop()

if __name__ == "__main__":
    main()
