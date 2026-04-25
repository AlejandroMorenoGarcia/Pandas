class Menu:
    def __init__(self):
        self.tablas = []

    def add_option(self, option):
        self.tablas.append(option)

    def print_options(self):
        for x in range(len(self.tablas)):
            print("{} - {}".format(x,self.tablas[x].getTitulo()))

    def get_option(self, option):
        self.tablas[option].getTabla()