import plotly.express as px
from GrupoTablas.Tablas import Tablas

class Tabla5(Tablas):
    """
    Clase especializada para la generación de un análisis visual entre el sueño y el rendimiento.
    
    Esta clase hereda de 'Tablas' y utiliza gráficos de violín para representar la distribución
    de las puntuaciones de exámenes en función de las horas de sueño reportadas por los estudiantes.
    
    Atributos:
        df (pd.DataFrame): Conjunto de datos que contiene al menos las columnas 'Sleep_Hours' y 'Exam_Score'.
        titulo (str): Título descriptivo del gráfico heredado de la clase base.
    """

    def __init__(self, df):
        """
        Inicializa la clase Tabla5 con el dataframe proporcionado.
        
        Args:
            df (pd.DataFrame): El DataFrame con los datos académicos y de hábitos de sueño.
        
        Note:
            Llama al constructor de la clase superior (super()) para establecer el título 
            "¿Dormir más mejora el rendimiento?".
        """
        super().__init__(df, "¿Dormir más mejora el rendimiento?")

    def getTabla(self):
        """
        Genera y despliega un gráfico de violín interactivo utilizando Plotly Express.
        
        El proceso realiza las siguientes subtareas:
        1.  Definición de un mapeo de colores semántico según la cantidad de horas de sueño.
        2.  Conversión de la columna 'Sleep_Hours' a tipo string para un tratamiento categórico en el eje X.
        3.  Configuración de un gráfico de violín que incluye:
            - Box plot interno (box=True) para ver cuartiles.
            - Representación de todos los puntos de datos (points="all").
            - Ordenamiento lógico de las categorías de 4 a 10 horas.
            - Estética 'dark mode' para la visualización.

        Returns:
            None: La función muestra el gráfico directamente mediante fig.show().
        """
        
        # Diccionario que asigna colores específicos a cada categoría de horas de sueño
        # para facilitar la interpretación visual (gradiente de alerta a descanso).
        color_discrete_map = {
            "4": "#FF6B6B",  # rojo coral         - poco sueño
            "5": "#FF9F43",  # naranja            - sueño insuficiente
            "6": "#FFC300",  # amarillo           - sueño escaso
            "7": "#4ECDC4",  # turquesa           - sueño adecuado
            "8": "#1DD1A1",  # verde menta        - sueño óptimo
            "9": "#48DBFB",  # azul celeste       - sueño largo
            "10": "#A29BFE"  # lavanda            - sueño excesivo
        }

        # Se crea una columna auxiliar de texto para que Plotly trate las horas como etiquetas discretas
        self.df["Sleep_Hours_Str"] = self.df["Sleep_Hours"].astype(str)

        # Creación de la figura interactiva
        fig = px.violin(
            self.df,
            box=True,                       # Dibuja un diagrama de caja dentro del violín
            points="all",                   # Muestra los puntos individuales al lado del violín
            x='Sleep_Hours_Str',            # Eje horizontal: Horas (Categoría)
            y='Exam_Score',                 # Eje vertical: Calificación (Variable continua)
            title=self.titulo,              # Título definido en el constructor
            color="Sleep_Hours_Str",        # Diferenciación de color por grupo
            color_discrete_map=color_discrete_map,
            labels={                        # Renombrado de etiquetas para la interfaz de usuario
                'Sleep_Hours_Str': 'Horas de Sueño',
                'Exam_Score': 'Puntuación del Examen',
            },
            # Asegura que las horas aparezcan en orden numérico y no alfabético
            category_orders={"Sleep_Hours_Str": ["4", "5", "6", "7", "8", "9", "10"]},
            template='plotly_dark'          # Estilo visual oscuro
        )

        # Renderización del gráfico en el navegador o entorno de ejecución
        fig.show()