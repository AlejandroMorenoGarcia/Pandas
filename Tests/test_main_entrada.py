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
    n = _num_tablas(main_mod)
    salir = str(n + 1)  # valor que hace salir del bucle, calculado dinámicamente
    secuencia = iter(list(entradas) + [salir])
    llamadas = []

    monkeypatch.setattr("builtins.input", lambda _prompt="": next(secuencia))
    monkeypatch.setattr(main_mod.Menu, "print_options", lambda self: None)
    monkeypatch.setattr(main_mod.Menu, "get_option", lambda self, opcion: llamadas.append(opcion))

    main_mod.main()
    return llamadas


def _num_tablas(main_mod) -> int:
    """Devuelve el número de tablas registradas en main, sin depender de valores hardcodeados."""
    import inspect, ast, pathlib
    src = pathlib.Path(inspect.getfile(main_mod)).read_text(encoding="utf-8")
    tree = ast.parse(src)
    count = sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "add_option"
    )
    return count


def test_main_reintenta_tras_texto_hasta_entero_valido(main_mod, monkeypatch):
    # "2" siempre cae dentro del rango válido (hay al menos 2 tablas)
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, ["abc", "2"])
    assert llamadas == [2 - 1]  # get_option recibe índice base-0


def test_main_acepta_limites_validos_del_menu(main_mod, monkeypatch):
    """El límite inferior es 1 y el superior es el número total de tablas."""
    n = _num_tablas(main_mod)
    limite_inferior = "1"
    limite_superior = str(n)

    llamadas_inf = _run_main_with_inputs(main_mod, monkeypatch, [limite_inferior])
    assert llamadas_inf == [0]  # opción 1 → índice 0

    llamadas_sup = _run_main_with_inputs(main_mod, monkeypatch, [limite_superior])
    assert llamadas_sup == [n - 1]  # opción n → índice n-1


def test_main_acepta_entero_con_espacios(main_mod, monkeypatch):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, [" 2 "])
    assert llamadas == [2 - 1]


@pytest.mark.parametrize("entrada_invalida", ["", "   ", "3.7", "texto"])
def test_main_reintenta_tras_no_entero(main_mod, monkeypatch, entrada_invalida):
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, [entrada_invalida, "1"])
    assert llamadas == [0]  # opción 1 → índice 0


def test_main_reintenta_tras_entero_fuera_de_rango(main_mod, monkeypatch):
    """Valores fuera de rango: 0, dos por encima del límite superior y un número muy alto.
    Nota: n+1 no se usa aquí porque _run_main_with_inputs ya lo añade como señal de salida.
    """
    n = _num_tablas(main_mod)
    fuera_de_rango = ["0", str(n + 2), "99"]
    for valor in fuera_de_rango:
        llamadas = _run_main_with_inputs(main_mod, monkeypatch, [valor, "1"])
        assert llamadas == [0], f"Se esperaba reintento tras entrada fuera de rango: {valor!r}"


def test_main_reintenta_hasta_recibir_opcion_valida(main_mod, monkeypatch):
    n = _num_tablas(main_mod)
    llamadas = _run_main_with_inputs(main_mod, monkeypatch, ["abc", "99", "0", str(n)])
    assert llamadas == [n - 1]