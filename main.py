from DataFrame import DataFrame
from Menu import Menu
from Tabla1 import Tabla1



def main():
    df_object = DataFrame()
    df = df_object.getdf()
    menu = Menu()
    menu.add_option(Tabla1(df))
    menu.print_options()
    opcion = int(input("Escoje una opcion: "))
    menu.get_option(opcion)


if __name__ == "__main__":
    main()