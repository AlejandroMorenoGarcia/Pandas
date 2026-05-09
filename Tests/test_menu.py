"""Pruebas del menú sin cambiar Menu.py."""

from __future__ import annotations

import pytest

from Menu import Menu


class _FakeTabla:
    def __init__(self, titulo):
        self._titulo = titulo

    def getTitulo(self):
        return self._titulo

    def getTabla(self):
        self.called = True


def test_menu_add_y_get_option_llama_gettabla():
    menu = Menu()
    fake = _FakeTabla("Prueba")
    menu.add_option(fake)
    menu.get_option(0)
    assert getattr(fake, "called", False)


def test_menu_indices_invalidos_lanzan_index_error(df_loaded):
    from GrupoTablas.Tabla1 import Tabla1

    menu = Menu()
    menu.add_option(Tabla1(df_loaded))

    with pytest.raises(IndexError):
        menu.get_option(1)


@pytest.mark.parametrize("indice_valido", [0, 4])
def test_menu_limites_validos_con_cinco_opciones(df_loaded, indice_valido):
    menu = _menu_con_cinco_tablas(df_loaded)
    menu.get_option(indice_valido)


def test_menu_cinco_opciones_con_proyecto_real(df_loaded):
    from GrupoTablas.Tabla1 import Tabla1
    from GrupoTablas.Tabla2 import Tabla2
    from GrupoTablas.Tabla3 import Tabla3
    from GrupoTablas.Tabla4 import Tabla4
    from GrupoTablas.Tabla5 import Tabla5

    menu = Menu()
    for cls in (Tabla1, Tabla2, Tabla3, Tabla4, Tabla5):
        menu.add_option(cls(df_loaded))

    assert len(menu.tablas) == 5


def _menu_con_cinco_tablas(df_loaded):
    from GrupoTablas.Tabla1 import Tabla1
    from GrupoTablas.Tabla2 import Tabla2
    from GrupoTablas.Tabla3 import Tabla3
    from GrupoTablas.Tabla4 import Tabla4
    from GrupoTablas.Tabla5 import Tabla5

    menu = Menu()
    for cls in (Tabla1, Tabla2, Tabla3, Tabla4, Tabla5):
        menu.add_option(cls(df_loaded))
    return menu


@pytest.mark.parametrize(
    "indice_fuera_de_rango",
    [
        -1,
        5,
        10,
        999,
    ],
)
def test_menu_cinco_opciones_indice_fuera_de_rango_lanza_index_error(
    df_loaded, indice_fuera_de_rango
):
    menu = _menu_con_cinco_tablas(df_loaded)

    with pytest.raises(IndexError):
        menu.get_option(indice_fuera_de_rango)


@pytest.mark.parametrize("indice_invalido", ["2", None, 2.5])
def test_menu_rechaza_indices_no_enteros(df_loaded, indice_invalido):
    menu = _menu_con_cinco_tablas(df_loaded)
    with pytest.raises(TypeError):
        menu.get_option(indice_invalido)
