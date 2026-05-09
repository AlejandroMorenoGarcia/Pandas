"""
Tests de comportamiento ideal del flujo de entrada en main().

Objetivo ideal:
- Si el usuario mete texto/no entero, se vuelve a pedir.
- Si mete un entero fuera de rango, se vuelve a pedir.
- Solo se llama get_option cuando la opción es válida (0..4).
"""

from __future__ import annotations

import pytest


@pytest.fixture
def main_mod():
    import main

    return main


def _run_main_with_inputs(main_mod, monkeypatch, entradas):
    secuencia = iter(entradas)
    llamadas = []

    monkeypatch.setattr("builtins.input", lambda _prompt="": next(secuencia))
    monkeypatch.setattr(main_mod.Menu, "print_options", lambda self: None)
    monkeypatch.setattr(main_mod.Menu, "get_option", lambda self, opcion: llamadas.append(opcion))

    main_mod.main()
    return llamadas


def test_main_reintenta_tras_texto_hasta_entero_valido(main_mod, monkeypatch):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, ["abc", "2"])
    assert llamadas == [2]


@pytest.mark.parametrize("entrada_valida", ["0", "4"])
def test_main_acepta_limites_validos_del_menu(main_mod, monkeypatch, entrada_valida):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, [entrada_valida])
    assert llamadas == [int(entrada_valida)]


def test_main_acepta_entero_con_espacios(main_mod, monkeypatch):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, [" 2 "])
    assert llamadas == [2]


@pytest.mark.parametrize("entrada_invalida", ["", "   ", "3.7", "texto"])
def test_main_reintenta_tras_no_entero(main_mod, monkeypatch, entrada_invalida):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, [entrada_invalida, "1"])
    assert llamadas == [1]


@pytest.mark.parametrize("fuera_rango", ["-1", "5", "99"])
def test_main_reintenta_tras_entero_fuera_de_rango(main_mod, monkeypatch, fuera_rango):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, [fuera_rango, "0"])
    assert llamadas == [0]


def test_main_reintenta_hasta_recibir_opcion_valida(main_mod, monkeypatch):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, ["abc", "99", "-1", "3"])
    assert llamadas == [3]
