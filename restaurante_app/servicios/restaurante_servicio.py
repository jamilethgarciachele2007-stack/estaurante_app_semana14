from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, ruta_productos: str, ruta_usuarios: str):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.productos = []
        self.usuarios = []
        self.cargar_datos()

    def cargar_datos(self):
        datos_prod = ArchivoServicio.leer_json(self.ruta_productos)
        self.productos = [Producto.desde_diccionario(p) for p in datos_prod]

        datos_usr = ArchivoServicio.leer_json(self.ruta_usuarios)
        self.usuarios = [Usuario.desde_diccionario(u) for u in datos_usr]

    def validar_acceso(self, username: str, password: str) -> Usuario:
        for u in self.usuarios:
            if u.username == username and u.password == password:
                return u
        return None

    def obtener_productos(self) -> list:
        return self.productos

    def obtener_usuarios(self) -> list:
        return self.usuarios