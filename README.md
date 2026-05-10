# 📊 Librería de Análisis del Rendimiento Estudiantil con Pandas

## 📌 Descripción

Proyecto en Python para explorar un conjunto de datos sobre factores de rendimiento académico. A partir de preguntas definidas, el programa ofrece un menú interactivo que genera visualizaciones (principalmente con **Plotly**) y, en algunos casos, tablas resumen en consola.

Los datos se cargan desde CSV mediante **Pandas**; cada opción del menú corresponde a un análisis distinto implementado en la carpeta `GrupoTablas`.

---

## 🎯 Objetivos

- Plantear preguntas relevantes sobre los datos.
- Procesar y agrupar la información con Pandas.
- Representar los resultados con gráficos claros (scatter, barras, violin, etc.).
- Facilitar la interpretación de patrones y relaciones entre variables.

---

## 🛠️ Tecnologías utilizadas

- Python 3
- Pandas
- Plotly Express
- Statsmodels
- Pytest
- Pathlib

---

## 📂 Estructura del proyecto

```
StudentsPerformance/
├── CSVs/
│   ├── StudentPerformanceFactors.csv
│   └── StudentPerformanceFactors_realistic.csv   
├── Documentacion/
│   ├── Documentacion Código/
│   │   ├── DocumentacionTabla1.html … DocumentacionTabla5.html
│   │   ├── DocumentacionTablas.html
│   │   ├── DocumentacionDataframe.html
│   │   ├── DocumentacionMain.html
│   │   └── DocumentacionMenu.html
│   ├── Informe de análisis del dataset/
│   │   └── Informe de análisis del dataset Alejandro,Axel e Iván.pdf
│   ├── Informe sobre librerias/
│   │   └── Informe sobre librerias Alejandro,Axel e Iván.pdf
│   └── Reflexión Individual y Conjunta/
│       ├── Reflexión Conjunta Alejandro,Axel e Iván.pdf
│       └── Reflexión Individual Alejandro.pdf
│       └── Reflexión Individual Iván.pdf
├── Libreria/
│   ├── DataFrame.py      
│   ├── Menu.py           
│   ├── main.py           
│   └── GrupoTablas/
│       ├── Tablas.py     
│       └── Tabla1.py … Tabla5.py
├── Tests/
│   ├── conftest.py
│   ├── test_dataframe_load.py
│   ├── test_main_entrada.py
│   ├── test_menu.py
│   └── test_tablas_smoke.py
└── README.md
```

La ruta del fichero de datos está definida en `DataFrame.py` y apunta a `CSVs/StudentPerformanceFactors_realistic.csv` (relativa a la carpeta `Libreria`).

---

## ⚙️ Instalación

1. Clonar el repositorio (ajusta la URL si tu remoto es distinto). La carpeta raíz del clon debe contener `Libreria/` y `CSVs/`:

```bash
git clone https://github.com/AlejandroMorenoGarcia/Pandas.git
cd Pandas
```

Si ya tienes el proyecto en local, sitúate en esa raíz y continúa con las dependencias.

2. Instalar dependencias:

```bash
pip install pandas plotly statsmodels
```

En Windows también puedes usar `py -m pip install pandas plotly statsmodels`.

---

## ▶️ Uso

Desde la carpeta `Libreria` (para que resuelvan bien los imports):

```bash
cd Libreria
python main.py
```

En Linux o macOS suele usarse `python3 main.py`.

El programa muestra un menú numerado. Introduce el número de la opción deseada:

| Opción | Pregunta / tema |
|--------|------------------|
| 1 | ¿Influye la asistencia y las horas de estudio en las notas? (scatter 3D) |
| 2 | ¿Cómo afecta la calidad del profesor a la mejora de las notas? (scatter con tendencia) |
| 3 | ¿Existe relación entre nivel socioeconómico y notas? (barras) |
| 4 | ¿El acceso a recursos e internet marca diferencias relevantes? (tabla en consola + barras) |
| 5 | ¿Dormir más mejora el rendimiento? (violin plot) |

Las figuras se abren en el navegador por defecto de Plotly.

---

## ✅ Tests

Para ejecutar los tests:

```bash
pip install pytest
python -m pytest Tests -v
```

Notas:

- Los tests están en la carpeta `Tests/`.
- `conftest.py` añade `Libreria` al `sys.path` para no tocar el código fuente.
- Hay pruebas de comportamiento actual y pruebas de comportamiento ideal del menú/entrada.

---

## ❓ Ejemplos de preguntas

Las mismas preguntas guían los distintos análisis del menú:

- ¿Influye la asistencia y las horas de estudio en las notas?
- ¿Cómo afecta la calidad del profesor a la mejora de las notas?
- ¿Existe relación entre nivel socioeconómico y notas?
- ¿El acceso a recursos e internet marca diferencias relevantes?
- ¿Dormir más mejora el rendimiento?

---

## 📈 Resultados

La librería genera tablas y gráficos que permiten:

- Resumir datos
- Comparar variables
- Identificar patrones y tendencias

---

## 🚧 Estado del proyecto

En desarrollo; se pueden añadir nuevas tablas extendiendo `GrupoTablas` y registrándolas en `main.py`.

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT.

---

## 👥 Autores

- Alejandro Moreno García
- Iván Fernández Saura
- Axel Abel Torres Valdez
- Andrei Danaila Cinco

---
