from DataFrame import DataFrame
from Menu import Menu
from GrupoTablas.Tabla1 import Tabla1
from GrupoTablas.Tabla2 import Tabla2
from GrupoTablas.Tabla3 import Tabla3
from GrupoTablas.Tabla4 import Tabla4
from GrupoTablas.Tabla5 import Tabla5


def main():
    df_object = DataFrame()
    df = df_object.getdf()
    menu = Menu()
    menu.add_option(Tabla1(df))
    menu.add_option(Tabla2(df))
    menu.add_option(Tabla3(df))
    menu.add_option(Tabla4(df))
    menu.add_option(Tabla5(df))
    menu.print_options()
    opcion = int(input("Escoje una opcion: "))
    menu.get_option(opcion)


if __name__ == "__main__":
    main()