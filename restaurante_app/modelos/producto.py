class Producto:
    def __init__(self, id: int, nombre: str, precio: float, categoria: str, stock: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            id=datos.get("id", 0),
            nombre=datos.get("nombre", ""),
            precio=float(datos.get("precio", 0.0)),
            categoria=datos.get("categoria", ""),
            stock=int(datos.get("stock", 0))
        )