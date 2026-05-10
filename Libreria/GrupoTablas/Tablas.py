"""
    Clase padre de todas las tablas de la libreria
"""
class Tablas:
    # Constructor de la clase
    def __init__(self, df, titulo):
        self.df = df
        self.titulo = titulo

    # Funcion general de la creacion de las tablas
    def getTabla(self):
        print("Tabla aun no creada")

    # Getter del titulo de la tabla
    def getTitulo(self):
        return self.titulo