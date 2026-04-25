import plotly.express as px
from Tablas import Tablas

class Tabla1(Tablas):
    def __init__(self,df):
        super().__init__(df, "Notas respecto a % de Clases Atendidas y Horas de Estudio")

    def getTabla(self):
        color_discrete_map = {
            "Male": "#2979FF",  # azul eléctrico
            "Female": "#FF1744"  # rojo/rosa intenso
        }

        df_largo = self.df.groupby(["Hours_Studied", "Exam_Score", "Gender", "Attendance"]).size().reset_index(name="Count")

        print(df_largo)

        fig = px.scatter_3d(df_largo, x="Hours_Studied", y="Attendance", z="Exam_Score", color="Gender",
                            color_discrete_map=color_discrete_map, size="Count", template="plotly_dark", size_max=30)
        fig.update_traces(marker=dict(
            line=dict(
                width=0,
                color="black"
            )
        ))
        fig.show(renderer="browser")