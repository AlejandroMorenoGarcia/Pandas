import plotly.express as px
from Tablas import Tablas


class Tabla5(Tablas):
    def __init__(self, df):
        
        super().__init__(df, "¿Dormir más mejora el rendimiento?")

    def getTabla(self):
        color_discrete_map = {
            "4": "#FF6B6B",  # rojo coral        - poco sueño
            "5": "#FF9F43",  # naranja           - sueño insuficiente
            "6": "#FFC300",  # amarillo          - sueño escaso
            "7": "#4ECDC4",  # turquesa          - sueño adecuado
            "8": "#1DD1A1",  # verde menta       - sueño óptimo
            "9": "#48DBFB",  # azul celeste      - sueño largo
            "10": "#A29BFE"  # lavanda           - sueño excesivo
        }

        self.df["Sleep_Hours_Str"] = self.df["Sleep_Hours"].astype(str)

        fig = px.violin(
            self.df,
            box=True,
            points="all",
            x='Sleep_Hours_Str',
            y='Exam_Score',
            title=self.titulo,
            color= "Sleep_Hours_Str",
            color_discrete_map= color_discrete_map,
            labels={
                'Sleep_Hours_Str': 'Horas de Sueño',
                'Exam_Score': 'Puntuación del Examen',
            },
            category_orders={"Sleep_Hours_Str": ["4", "5", "6", "7", "8", "9", "10"]},
            template='plotly_dark'
        )

        fig.show()