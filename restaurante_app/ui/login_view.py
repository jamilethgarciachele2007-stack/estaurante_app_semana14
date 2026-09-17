import tkinter as tk

class LoginView(tk.Frame):
    def __init__(self, master, servicio, al_ingresar_exitoso):
        super().__init__(master)
        self.servicio = servicio
        self.al_ingresar_exitoso = al_ingresar_exitoso
        self.crear_componentes()

    def crear_componentes(self):
        # Título
        lbl_titulo = tk.Label(self, text="Acceso al Sistema - Restaurante App", font=("Helvetica", 14, "bold"))
        lbl_titulo.pack(pady=20)

        # Contenedor del Formulario
        frame_form = tk.Frame(self)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Usuario:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.txt_usuario = tk.Entry(frame_form)
        self.txt_usuario.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Contraseña:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.txt_password = tk.Entry(frame_form, show="*")
        self.txt_password.grid(row=1, column=1, padx=5, pady=5)

        # Mensaje de retroalimentación visual
        self.lbl_mensaje = tk.Label(self, text="", fg="red")
        self.lbl_mensaje.pack(pady=5)

        # Botón de Ingreso
        btn_ingresar = tk.Button(self, text="Iniciar Sesión", command=self.validar, bg="#4CAF50", fg="white", padx=10, pady=3)
        btn_ingresar.pack(pady=10)

    def validar(self):
        usuario_val = self.txt_usuario.get().strip()
        password_val = self.txt_password.get().strip()

        # Validación 1: Campos vacíos
        if not usuario_val or not password_val:
            self.lbl_mensaje.config(text="Por favor, complete todos los campos.")
            return

        # Validación 2: Credenciales a través de RestauranteServicio
        usuario_autenticado = self.servicio.validar_acceso(usuario_val, password_val)

        if usuario_autenticado:
            self.lbl_mensaje.config(text="")
            self.txt_usuario.delete(0, tk.END)
            self.txt_password.delete(0, tk.END)
            self.al_ingresar_exitoso(usuario_autenticado)
        else:
            self.lbl_mensaje.config(text="Credenciales incorrectas. Intente nuevamente.")