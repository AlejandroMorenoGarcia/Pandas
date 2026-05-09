"""Smoke tests: cada tabla debe ejecutarse sin error (fig.show está anulado en conftest)."""

from __future__ import annotations

from GrupoTablas.Tabla1 import Tabla1
from GrupoTablas.Tabla2 import Tabla2
from GrupoTablas.Tabla3 import Tabla3
from GrupoTablas.Tabla4 import Tabla4
from GrupoTablas.Tabla5 import Tabla5


def test_tabla1_gettabla(df_loaded):
    Tabla1(df_loaded).getTabla()


def test_tabla2_gettabla(df_loaded):
    Tabla2(df_loaded).getTabla()


def test_tabla3_gettabla(df_loaded):
    Tabla3(df_loaded).getTabla()


def test_tabla4_gettabla(df_loaded, capsys):
    Tabla4(df_loaded).getTabla()
    captured = capsys.readouterr().out
    assert "Acceso a Internet" in captured or "Internet" in captured


def test_tabla5_gettabla(df_loaded):
    Tabla5(df_loaded).getTabla()


def test_titulos_coinciden_con_menu(df_loaded):
    esperados = [
        "¿Influye la asistencia y las horas de estudio en las notas?",
        "¿Cómo afecta la calidad del profesor a la mejora de las notas?",
        "¿Existe relación entre nivel socioeconómico y notas?",
        "¿El acceso a recursos e internet marca diferencias relevantes?",
        "¿Dormir más mejora el rendimiento?",
    ]
    tablas = [
        Tabla1(df_loaded),
        Tabla2(df_loaded),
        Tabla3(df_loaded),
        Tabla4(df_loaded),
        Tabla5(df_loaded),
    ]
    assert [t.getTitulo() for t in tablas] == esperados
