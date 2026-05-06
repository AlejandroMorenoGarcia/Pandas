import plotly.express as px
from Tablas import Tablas

# Grafivo sobre la importancia de los profesores en la mejora de las notas
class Tabla2(Tablas):
    # Constructor de la clase
    def __init__(self,df):
        super().__init__(df, "¿Cómo afecta la calidad del profesor a la mejora de las notas?")

    # Funcion de la creacion de la tabla
    def getTabla(self):
        """
            Esta grafica utilizaremos utilizaremos el Data Frame principal sin modificaciones 
            ya que no sera necesario para la obtencion de los datos que ya tenemos
        """

        # Variable para los colores de los posibles valores
        color_discrete_map = {
            "Low": "#FF6B6B",  # rojo coral
            "Medium": "#4ECDC4",  # turquesa
            "High": "#FFE66D",  # amarillo dorado
        }

        # Creacion de la grafica
        fig = px.scatter(
            self.df, # Data Frame principar
            x="Previous_Scores", # Eje X: Anteriores notas
            y="Exam_Score", # Eje Y: Notas actuales
            color="Teacher_Quality",  # Color por calidad del profesor
            trendline="lowess", # Linea de tendencia de las graficas para cada calidad del profesor 
            trendline_options = {"frac": 0.2}, # 
            title=self.titulo, # Titulo de la grafica
            labels={ # Renombre de las distintas opciones
                "Previous_Scores": "Puntuaciones Anteriores",
                "Exam_Score": "Puntuación del Examen",
                "Teacher_Quality": "Calidad del Profesor",
            },
            opacity=0.6, # Opacidad de los valores
            template="plotly_dark", # Estilo de fondo de la Grafica
            color_discrete_map= color_discrete_map # Opciones de los colores
        )
        """
            Vamos a generar una linea extra que pase por la diagonal para ver los 
            alumnos que han mejorado su nota y los que la han empeorado
        """

        min_val = self.df["Exam_Score"].min() # Variable para el valor minimo de la diagonal
        max_val = 100 # Variable para el valor maximo de la diagonal

        # Creacion de la linea 
        fig.add_shape( # Añadimos a la figura la linea
            type="line", # Tipo Linea
            x0=min_val, y0=min_val, # Valores minimos de la linea en los ejes 
            x1=max_val, y1=max_val, # Valores maximos de la linea en los ejes 
            line=dict( # Opciones de la linea
                color="white", # Color Blanco
                width=2, # Ancho
                dash="dash" # Tipo punteado
            )
        )

        # La añadimos a la leyenda
        fig.add_scatter(
            x=[None], y=[None],
            mode="lines",
            line=dict(color="white", width=2, dash="dash"),
            name="Referencia y=x"
        )

        fig.show() # Mostramos la grafica