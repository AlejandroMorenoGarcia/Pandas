
"""
    Clase de menu que guanda todas las Tablas de la libreria para
    poder escojer en cada momento cual de las graficas ver
"""
class Menu:
    # Constructor de la clase
    def __init__(self):
        self.tablas = []

    # Funcion para añadir las tablas al menu
    def add_option(self, option):
        self.tablas.append(option)

    # Funcion para mostrar las tablas
    def print_options(self):
        for x in range(len(self.tablas)):
            print("{} - {}".format(x,self.tablas[x].getTitulo()))

    # Funcion para escojer la tabla y mostrarla
    def get_option(self, option):
        self.tablas[option].getTabla()