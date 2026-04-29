import plotly.express as px
from Tablas import Tablas

class Tabla2(Tablas):
    def __init__(self,df):
        super().__init__(df, "¿Cómo afecta la calidad del profesor a la mejora de las notas?")

    def getTabla(self):
        color_discrete_map = {
            "Low": "#FF6B6B",  # rojo coral
            "Medium": "#4ECDC4",  # turquesa
            "High": "#FFE66D",  # amarillo dorado
        }

        fig = px.scatter(
            self.df,
            x="Previous_Scores",
            y="Exam_Score",
            color="Teacher_Quality",  # color por calidad del profesor
            trendline="lowess",
            trendline_options = {"frac": 0.2},
            title=self.titulo,
            labels={
                "Previous_Scores": "Puntuaciones Anteriores",
                "Exam_Score": "Puntuación del Examen",
                "Teacher_Quality": "Calidad del Profesor",
            },
            opacity=0.6,
            template="plotly_dark",
            color_discrete_map= color_discrete_map
        )

        min_val = self.df["Exam_Score"].min()
        max_val = 100

        fig.add_shape(
            type="line",
            x0=min_val, y0=min_val,
            x1=max_val, y1=max_val,
            line=dict(
                color="white",
                width=2,
                dash="dash"  
            )
        )

        # Añadir a la leyenda
        fig.add_scatter(
            x=[None], y=[None],
            mode="lines",
            line=dict(color="white", width=2, dash="dash"),
            name="Referencia y=x"
        )

        fig.show()