"""Comprobaciones sobre la carga del CSV y columnas usadas por las tablas."""

from __future__ import annotations

# noqa: conftest añade Libreria al path antes de importar vía pytest

REQUIRED_COLUMNS = {
    "Hours_Studied",
    "Exam_Score",
    "Gender",
    "Attendance",
    "Previous_Scores",
    "Teacher_Quality",
    "Family_Income",
    "Internet_Access",
    "Sleep_Hours",
}


def test_dataframe_no_esta_vacio(df_loaded):
    assert len(df_loaded) > 0


def test_dataframe_tiene_columnas_necesarias(df_loaded):
    faltan = REQUIRED_COLUMNS - set(df_loaded.columns)
    assert not faltan, f"Faltan columnas en el CSV: {faltan}"
