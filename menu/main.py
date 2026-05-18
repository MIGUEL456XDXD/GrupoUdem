from _4_sistema.sistema_estudio import SistemaEstudio
from _5_interfaz.dashboard import Dashboard

def main():
    sistema = SistemaEstudio()
    app = Dashboard(sistema)
    app.mainloop()

if __name__ == "__main__":
    main()
