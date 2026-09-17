import os
import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Restaurante App - Interfaz Gráfica")
        self.geometry("650x450")
        self.minsize(550, 400)

        # Construcción de rutas dinámicas a los datos JSON
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_prod = os.path.join(base_dir, "datos", "productos.json")
        ruta_usr = os.path.join(base_dir, "datos", "usuarios.json")

        # Inicialización del servicio
        self.servicio = RestauranteServicio(ruta_prod, ruta_usr)

        self.vista_actual = None
        self.mostrar_login()

    def mostrar_login(self):
        if self.vista_actual:
            self.vista_actual.destroy()

        self.vista_actual = LoginView(self, self.servicio, self.mostrar_main)
        self.vista_actual.pack(expand=True, fill="both")

    def mostrar_main(self, usuario_autenticado):
        if self.vista_actual:
            self.vista_actual.destroy()

        self.vista_actual = MainView(self, self.servicio, usuario_autenticado, self.mostrar_login)
        self.vista_actual.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = App()
    app.mainloop()