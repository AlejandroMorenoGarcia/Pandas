import plotly.express as px
from GrupoTablas.Tablas import Tablas

# Grafico sobre la influencia de la asistencia y las horas de estudio en las notas
class Tabla1(Tablas):
    # Constructor de la clase
    def __init__(self,df):
        super().__init__(df, "¿Influye la asistencia y las horas de estudio en las notas?")

    # Funcion de la creacion de la tabla
    def getTabla(self):
        """
            En esta grafica vamos a comprobar la importancia de atender a clase y
            las horas que estudiamos a la hora de la mejora de nuestras notas en la
            que modificaremos nuestro Data Frame principal para poder hacer un 
            count de la las agrupaciones que coincidan para hacer los puntos de 
            la tabla mas grandes segun este count
        """

        # Variable para los colores de los posibles valores
        color_discrete_map = {
            "Male": "#2979FF",  # azul eléctrico
            "Female": "#FF1744"  # rojo/rosa intenso
        }

        # Modificamos el Data Frame principal para quedarnos con las columnas que queremos y añadir el count
        df_largo = self.df.groupby(["Hours_Studied", "Exam_Score", "Gender", "Attendance"]).size().reset_index(name="Count")

        # Creacion de la grafica
        fig = px.scatter_3d(
            df_largo, # Data Frame modificado
            x="Hours_Studied", # Eje X: Horas de estudio
            y="Attendance", # Eje Y: Atencion en clase
            z="Exam_Score", # Eje Z: Notas de los examenes
            title=self.titulo, # Titulo de la grafica
            color="Gender", # Color diferenciado por genero
            color_discrete_map=color_discrete_map, # Opciones de los colores
            size="Count", # Radio segun cantidad
            labels={ # Renombre de las distintas opciones
                "Hours_Studied": "Horas de Estudio",
                "Exam_Score": "Puntuación del Examen",
                "Attendance": "Asistencia a Clase",
            },
            template="plotly_dark", # Estilo de fondo de la Grafica
        )

        # Adaptamos la grafica para que tenga forma de cubo
        fig.update_layout(
            scene=dict(
                aspectmode="cube",
            )
        )

        # Quitamos el borde de los de los valores
        fig.update_traces(marker=dict(
            line=dict(
                width=0,
                color="black"
            )
        ))

        fig.show() # Mostramos la grafica