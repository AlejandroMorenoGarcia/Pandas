"""
Configuración local de pytest: añade Libreria/ al sys.path sin modificar el proyecto.
Ejecutar desde la raíz del repo: pytest Tests
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parent.parent
_LIBRERIA = _ROOT / "Libreria"

if str(_LIBRERIA) not in sys.path:
    sys.path.insert(0, str(_LIBRERIA))


@pytest.fixture(scope="module")
def df_loaded():
    from DataFrame import DataFrame

    return DataFrame().getdf()


@pytest.fixture(autouse=True)
def no_plotly_browser(monkeypatch):
    """Evita abrir el navegador al llamar a fig.show() en las tablas."""

    def _noop_show(self, *args, **kwargs):
        return None

    monkeypatch.setattr(
        "plotly.basedatatypes.BaseFigure.show",
        _noop_show,
        raising=True,
    )
