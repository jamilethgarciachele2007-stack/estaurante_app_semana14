# Restaurante App - Interfaz Gráfica (Semana 13)

## Descripción del Proyecto
`restaurante_app` es una aplicación desarrollada en Python utilizando Tkinter para la interfaz gráfica de usuario. Esta versión inicial realiza la transición desde la versión de consola hacia un entorno gráfico modular, siguiendo el patrón de arquitectura por capas (Modelos, Servicios, Vistas).

## Estructura de Capas
- **`datos/`**: Archivos `.json` para persistencia local de productos y usuarios.
- **`modelos/`**: Clases de dominio (`Producto`, `Usuario`) construidas mediante deserialización JSON.
- **`servicios/`**: 
  - `ArchivoServicio`: Lectura de archivos JSON locales.
  - `RestauranteServicio`: Gestión de lógica de negocio y validación de usuarios.
- **`ui/`**: 
  - `LoginView`: Pantalla de acceso simulación de login.
  - `MainView`: Panel principal con pestañas para productos, usuarios y ventas (pendiente).
- **`main.py`**: Punto de entrada de la aplicación que administra la ventana principal de Tkinter.

## Instrucciones de Ejecución
1. Clonar el repositorio.
2. Asegurarse de contar con Python 3.8+ instalado.
3. Ejecutar el archivo principal desde la terminal:
   ```bash
   python main.py

   ## Credenciales de prueba
Para iniciar sesión en la aplicación, puede utilizar los siguientes usuarios registrados en `datos/usuarios.json`:

- **Administrador:**
  - **Usuario:** `admin`
  - **Contraseña:** `123`

- **Mesero:**
  - **Usuario:** `mesero1`
  - **Contraseña:** `123`