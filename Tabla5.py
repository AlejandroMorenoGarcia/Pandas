import plotly.express as px
from Tablas import Tablas


class Tabla5(Tablas):
    def __init__(self, df):
        
        super().__init__(df, "¿Dormir más mejora el rendimiento?")

    def getTabla(self):
        
        color_discrete_map = {
            "Male": "#2979FF",  
            "Female": "#FF1744" 
        }

       
        fig = px.violin(
            self.df,
            box=True,
            points="all",
            x='Sleep_Hours',
            y='Exam_Score',
            color_discrete_map=color_discrete_map,
            title=self.titulo,
            labels={
                'Sleep_Hours': 'Horas de Sueño',
                'Exam_Score': 'Puntuación del Examen',
            },
            template='plotly_dark'
        )
        
        
        fig.show()
        
        


