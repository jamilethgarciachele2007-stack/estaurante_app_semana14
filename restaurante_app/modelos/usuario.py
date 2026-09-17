class Usuario:
    def __init__(self, username: str, password: str, nombre: str, rol: str):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            username=datos.get("username", ""),
            password=datos.get("password", ""),
            nombre=datos.get("nombre", ""),
            rol=datos.get("rol", "")
        )