from DataFrame import DataFrame
from Menu import Menu
from Tablas import Tabla1,Tabla2,Tabla3,Tabla4,Tabla5


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