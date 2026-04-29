import plotly.express as px
from Tablas import Tablas

class Tabla3(Tablas):
    #Constructo de la clase
    def __init__(self, df):
        super().__init__(df, "¿Existe relación entre nivel socioeconómico y notas?")

    
    #Función principal que agrupa los datos, crea el gráfico y muestra las figura
    def getTabla(self):
        #Función que agrupa
        df_grouped = self.df.groupby("Family_Income", as_index=False)["Exam_Score"].mean() #Función Media

        fig = px.bar(
            df_grouped,
            x="Family_Income",
            y="Exam_Score",
            text="Exam_Score",
            color="Family_Income",
            color_discrete_map={
                "Low": "#4C78A8",
                "Medium": "#54A24B",
                "High": "#F58518"
            },
            template="plotly_dark",
            labels={
                "Family_Income": "Nivel Socioeconómico",
                "Exam_Score": "Nota Media del Examen"
            }
        )

        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')

        fig.update_layout(
            xaxis_title="Nivel Socioeconómico",
            yaxis_title="Nota Media del Examen",
            title=self.titulo,
            yaxis_range=[68, 70]
        )

        fig.show()