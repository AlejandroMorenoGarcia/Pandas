import plotly.express as px
from Tablas import Tablas

class Tabla1(Tablas):
    def __init__(self,df):
        super().__init__(df, "¿Influye la asistencia y las horas de estudio en las notas?")

    def getTabla(self):
        color_discrete_map = {
            "Male": "#2979FF",  # azul eléctrico
            "Female": "#FF1744"  # rojo/rosa intenso
        }

        df_largo = self.df.groupby(["Hours_Studied", "Exam_Score", "Gender", "Attendance"]).size().reset_index(name="Count")

        fig = px.scatter_3d(
            df_largo,
            x="Hours_Studied",
            y="Attendance",
            z="Exam_Score",
            title=self.titulo,
            color="Gender",
            color_discrete_map=color_discrete_map,
            size="Count",
            labels={
                "Hours_Studied": "Horas de Estudio",
                "Exam_Score": "Puntuación del Examen",
                "Attendance": "Asistencia a Clase",
            },
            template="plotly_dark",
            size_max=30
        )

        fig.update_layout(
            xaxis_title="Nivel Socioeconómico",
            yaxis_title="Nota Media del Examen",
            title=self.titulo,
            scene=dict(
                aspectmode="cube",
            )
        )

        fig.update_traces(marker=dict(
            line=dict(
                width=0,
                color="black"
            )
        ))

        fig.show()