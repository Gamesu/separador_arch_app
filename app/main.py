# src/main.py
from interface_user import user_interface as ui

def main():
    # Iniciar la interfaz gráfica
    app = ui()
    app.start_app()

if __name__ == "__main__":
    main()
