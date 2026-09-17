import tkinter as tk
from tkinter import ttk, messagebox
from modelos.producto import Producto

class MainView(tk.Frame):
    def __init__(self, parent, servicio, usuario_actual, on_logout):
        super().__init__(parent, bg="#f1f5f9")
        self.parent = parent
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout

        self.crear_layout()
        self.mostrar_inicio()

    def crear_layout(self):
        # 1. CONTENEDOR LATERAL (Sidebar)
        self.sidebar = tk.Frame(self, bg="#1e293b", width=180)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="RESTAURANTE", font=("Arial", 12, "bold"), bg="#1e293b", fg="#ffffff").pack(pady=(15, 5))
        
        rol_texto = getattr(self.usuario_actual, 'rol', 'Administrador')
        tk.Label(self.sidebar, text=f"Rol: {rol_texto}", font=("Arial", 9), bg="#1e293b", fg="#94a3b8").pack(pady=(0, 15))

        btn_opts = {
            "font": ("Arial", 10),
            "bg": "#334155",
            "fg": "#ffffff",
            "activebackground": "#2563eb",
            "activeforeground": "#ffffff",
            "relief": "flat",
            "anchor": "w",
            "padx": 15,
            "cursor": "hand2"
        }
        
        tk.Button(self.sidebar, text="🏠  Inicio", command=self.mostrar_inicio, **btn_opts).pack(fill="x", pady=2)
        tk.Button(self.sidebar, text="👥  Usuarios", command=self.mostrar_usuarios, **btn_opts).pack(fill="x", pady=2)
        tk.Button(self.sidebar, text="🍔  Productos", command=self.mostrar_productos, **btn_opts).pack(fill="x", pady=2)

        tk.Button(
            self.sidebar, text="🚪  Cerrar sesión", bg="#ef4444", fg="#ffffff",
            font=("Arial", 9, "bold"), activebackground="#dc2626", activeforeground="#ffffff",
            relief="flat", cursor="hand2", command=self.on_logout
        ).pack(side="bottom", fill="x", pady=15, padx=10)

        # 2. CONTENEDOR CENTRAL
        self.area_contenido = tk.Frame(self, bg="#f8fafc")
        self.area_contenido.pack(side="right", expand=True, fill="both")

    def limpiar_contenido(self):
        for widget in self.area_contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()

        header = tk.Frame(self.area_contenido, bg="#f8fafc")
        header.pack(fill="x", padx=20, pady=15)
        tk.Label(header, text="Panel principal", font=("Arial", 18, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w")
        tk.Label(header, text="Consulte usuarios y gestione productos desde el menú lateral.", font=("Arial", 10), bg="#f8fafc", fg="#64748b").pack(anchor="w")

        cards_frame = tk.Frame(self.area_contenido, bg="#f8fafc")
        cards_frame.pack(fill="x", padx=20, pady=10)

        num_usr = len(self.obtener_lista_usuarios())
        num_prod = len(self.obtener_lista_productos())

        c1 = tk.Frame(cards_frame, bg="#ffffff", bd=1, relief="solid", padx=15, pady=15)
        c1.pack(side="left", expand=True, fill="both", padx=(0, 10))
        tk.Label(c1, text="Usuarios registrados", font=("Arial", 10, "bold"), bg="#ffffff", fg="#64748b").pack(anchor="w")
        tk.Label(c1, text=str(num_usr), font=("Arial", 24, "bold"), bg="#ffffff", fg="#2563eb").pack(anchor="w", pady=(5, 0))

        c2 = tk.Frame(cards_frame, bg="#ffffff", bd=1, relief="solid", padx=15, pady=15)
        c2.pack(side="left", expand=True, fill="both", padx=(10, 0))
        tk.Label(c2, text="Productos registrados", font=("Arial", 10, "bold"), bg="#ffffff", fg="#64748b").pack(anchor="w")
        tk.Label(c2, text=str(num_prod), font=("Arial", 24, "bold"), bg="#ffffff", fg="#2563eb").pack(anchor="w", pady=(5, 0))

    def obtener_lista_productos(self):
        for fn in ['obtener_productos', 'get_productos', 'listar_productos']:
            if hasattr(self.servicio, fn):
                return getattr(self.servicio, fn)()
        if hasattr(self.servicio, 'productos'):
            return self.servicio.productos
        return []

    def obtener_lista_usuarios(self):
        for fn in ['obtener_usuarios', 'get_usuarios', 'listar_usuarios']:
            if hasattr(self.servicio, fn):
                return getattr(self.servicio, fn)()
        if hasattr(self.servicio, 'usuarios'):
            return self.servicio.usuarios
        return []

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        header = tk.Frame(self.area_contenido, bg="#f8fafc")
        header.pack(fill="x", padx=20, pady=15)
        tk.Label(header, text="Usuarios del Sistema", font=("Arial", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w")

        table_frame = tk.Frame(self.area_contenido, bg="#ffffff", padx=10, pady=10)
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        cols = ("username", "nombre", "rol")
        tabla = ttk.Treeview(table_frame, columns=cols, show="headings")
        tabla.heading("username", text="Usuario")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("rol", text="Rol")
        tabla.pack(fill="both", expand=True)

        for u in self.obtener_lista_usuarios():
            if isinstance(u, dict):
                u_user = u.get('username', u.get('usuario', ''))
                u_nom = u.get('nombre', u_user)
                u_rol = u.get('rol', 'Usuario')
            else:
                u_user = getattr(u, 'username', getattr(u, 'usuario', ''))
                u_nom = getattr(u, 'nombre', u_user)
                u_rol = getattr(u, 'rol', 'Usuario')
            tabla.insert("", "end", values=(u_user, u_nom, u_rol))

    def mostrar_productos(self):
        self.limpiar_contenido()

        header = tk.Frame(self.area_contenido, bg="#f8fafc")
        header.pack(fill="x", padx=20, pady=10)
        tk.Label(header, text="Gestión de Productos", font=("Arial", 16, "bold"), bg="#f8fafc", fg="#0f172a").pack(anchor="w")

        body = tk.Frame(self.area_contenido, bg="#f8fafc")
        body.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        # Formulario a la Izquierda
        form = tk.Frame(body, bg="#ffffff", padx=10, pady=10, bd=1, relief="solid")
        form.pack(side="left", fill="y", padx=(0, 10))

        tk.Label(form, text="Datos del Producto", font=("Arial", 11, "bold"), bg="#ffffff").pack(anchor="w", pady=(0, 5))

        tk.Label(form, text="ID / Código:", bg="#ffffff", font=("Arial", 9)).pack(anchor="w")
        self.ent_id = tk.Entry(form, width=15)
        self.ent_id.pack(pady=(0, 5))

        tk.Label(form, text="Nombre:", bg="#ffffff", font=("Arial", 9)).pack(anchor="w")
        self.ent_nombre = tk.Entry(form, width=15)
        self.ent_nombre.pack(pady=(0, 5))

        tk.Label(form, text="Categoría:", bg="#ffffff", font=("Arial", 9)).pack(anchor="w")
        self.ent_categoria = tk.Entry(form, width=15)
        self.ent_categoria.pack(pady=(0, 5))

        tk.Label(form, text="Precio ($):", bg="#ffffff", font=("Arial", 9)).pack(anchor="w")
        self.ent_precio = tk.Entry(form, width=15)
        self.ent_precio.pack(pady=(0, 10))

        btn_style = {"width": 14, "font": ("Arial", 8, "bold"), "cursor": "hand2"}
        tk.Button(form, text="Registrar", bg="#16a34a", fg="white", command=self.btn_registrar, **btn_style).pack(pady=2)
        tk.Button(form, text="Cargar / Buscar", bg="#0284c7", fg="white", command=self.btn_cargar, **btn_style).pack(pady=2)
        tk.Button(form, text="Actualizar", bg="#eab308", fg="white", command=self.btn_actualizar, **btn_style).pack(pady=2)
        tk.Button(form, text="Eliminar", bg="#dc2626", fg="white", command=self.btn_eliminar, **btn_style).pack(pady=2)

        # Tabla a la Derecha
        table_container = tk.Frame(body, bg="#ffffff", bd=1, relief="solid")
        table_container.pack(side="right", fill="both", expand=True)

        cols = ("id", "nombre", "categoria", "precio")
        self.tabla_prod = ttk.Treeview(table_container, columns=cols, show="headings")
        self.tabla_prod.heading("id", text="ID")
        self.tabla_prod.heading("nombre", text="Nombre")
        self.tabla_prod.heading("categoria", text="Categoría")
        self.tabla_prod.heading("precio", text="Precio ($)")

        self.tabla_prod.column("id", width=50, minwidth=40)
        self.tabla_prod.column("nombre", width=110, minwidth=80)
        self.tabla_prod.column("categoria", width=100, minwidth=70)
        self.tabla_prod.column("precio", width=70, minwidth=50)

        scrollbar_y = ttk.Scrollbar(table_container, orient="vertical", command=self.tabla_prod.yview)
        self.tabla_prod.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_y.pack(side="right", fill="y")

        self.tabla_prod.pack(fill="both", expand=True, padx=5, pady=5)

        self.refrescar_tabla_productos()

    def refrescar_tabla_productos(self):
        for row in self.tabla_prod.get_children():
            self.tabla_prod.delete(row)
        
        for p in self.obtener_lista_productos():
            if isinstance(p, dict):
                p_id = p.get('id', p.get('id_producto', ''))
                p_nom = p.get('nombre', '')
                p_cat = p.get('categoria', '')
                p_pre = p.get('precio', 0.0)
            else:
                p_id = getattr(p, 'id', getattr(p, 'id_producto', ''))
                p_nom = getattr(p, 'nombre', '')
                p_cat = getattr(p, 'categoria', '')
                p_pre = getattr(p, 'precio', 0.0)

            self.tabla_prod.insert("", "end", values=(p_id, p_nom, p_cat, f"${float(p_pre):.2f}"))

    def ejecutar_metodo_servicio(self, nombres_posibles, *args):
        for nombre in nombres_posibles:
            if hasattr(self.servicio, nombre):
                metodo = getattr(self.servicio, nombre)
                try:
                    return metodo(*args)
                except TypeError:
                    try:
                        # Intenta pasar id como entero si es numérico
                        args_int = list(args)
                        if args_int and str(args_int[0]).isdigit():
                            args_int[0] = int(args_int[0])
                        return metodo(*args_int)
                    except Exception:
                        pass
        return None

    def btn_registrar(self):
        id_val = self.ent_id.get().strip()
        nombre_val = self.ent_nombre.get().strip()
        cat_val = self.ent_categoria.get().strip()
        precio_str = self.ent_precio.get().strip()

        if not id_val or not nombre_val or not cat_val or not precio_str:
            messagebox.showwarning("Atención", "Por favor complete todos los campos.")
            return

        try:
            precio_val = float(precio_str)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un precio numérico válido.")
            return

        nuevo_p = Producto(id_val, nombre_val, cat_val, precio_val)
        
        # Prueba ejecutar métodos comunes de registro
        res = self.ejecutar_metodo_servicio(['agregar_producto', 'registrar_producto', 'crear_producto'], nuevo_p)
        if res is None:
            res = self.ejecutar_metodo_servicio(['agregar_producto', 'registrar_producto', 'crear_producto'], id_val, nombre_val, cat_val, precio_val)

        if res is not False and res is not None:
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            self.refrescar_tabla_productos()
        else:
            messagebox.showwarning("Atención", "No se pudo registrar el producto.")

    def btn_cargar(self):
        id_val = self.ent_id.get().strip()
        if not id_val:
            messagebox.showwarning("Atención", "Ingrese el ID/Código para buscar.")
            return

        # Busca primero probando el ID como texto y luego como entero
        p = self.ejecutar_metodo_servicio(['buscar_producto_por_id', 'obtener_producto_por_id', 'buscar_producto', 'get_producto'], id_val)
        
        if not p and id_val.isdigit():
            p = self.ejecutar_metodo_servicio(['buscar_producto_por_id', 'obtener_producto_por_id', 'buscar_producto', 'get_producto'], int(id_val))

        # Si no lo encuentra por método, busca directamente en la lista de productos
        if not p:
            for item in self.obtener_lista_productos():
                item_id = item.get('id', item.get('id_producto')) if isinstance(item, dict) else getattr(item, 'id', getattr(item, 'id_producto', None))
                if str(item_id) == str(id_val):
                    p = item
                    break

        if p:
            if isinstance(p, dict):
                p_nom = p.get('nombre', '')
                p_cat = p.get('categoria', '')
                p_pre = p.get('precio', '')
            else:
                p_nom = getattr(p, 'nombre', '')
                p_cat = getattr(p, 'categoria', '')
                p_pre = getattr(p, 'precio', '')

            self.ent_nombre.delete(0, tk.END)
            self.ent_nombre.insert(0, p_nom)
            self.ent_categoria.delete(0, tk.END)
            self.ent_categoria.insert(0, p_cat)
            self.ent_precio.delete(0, tk.END)
            self.ent_precio.insert(0, str(p_pre))
            messagebox.showinfo("Éxito", "Datos del producto cargados.")
        else:
            messagebox.showwarning("Atención", "Producto no encontrado.")
    def btn_actualizar(self):
        id_val = self.ent_id.get().strip()
        nombre_val = self.ent_nombre.get().strip()
        cat_val = self.ent_categoria.get().strip()
        precio_str = self.ent_precio.get().strip()

        if not id_val:
            messagebox.showwarning("Atención", "Ingrese el ID del producto a actualizar.")
            return

        try:
            precio_val = float(precio_str)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un precio numérico válido.")
            return

        nuevo_p = Producto(id_val, nombre_val, cat_val, precio_val)
        res = self.ejecutar_metodo_servicio(['actualizar_producto', 'modificar_producto'], nuevo_p)
        if res is None:
            res = self.ejecutar_metodo_servicio(['actualizar_producto', 'modificar_producto'], id_val, nombre_val, cat_val, precio_val)

        if res is not False and res is not None:
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.refrescar_tabla_productos()
        else:
            messagebox.showwarning("Atención", "No se pudo actualizar el producto.")

    def btn_eliminar(self):
        id_val = self.ent_id.get().strip()
        if not id_val:
            messagebox.showwarning("Atención", "Ingrese el ID del producto a eliminar.")
            return

        res = self.ejecutar_metodo_servicio(['eliminar_producto', 'borrar_producto'], id_val)

        if res is not False and res is not None:
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.refrescar_tabla_productos()
        else:
            messagebox.showwarning("Atención", "No se pudo eliminar el producto.")