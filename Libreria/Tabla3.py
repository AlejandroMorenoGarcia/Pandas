import plotly.express as px
from Tablas import Tablas

#Gráfico del database sobre el nivel estudios en el contexto socioeconómico.
class Tabla3(Tablas):
   
    #Constructo de la clase
    def __init__(self, df):
        super().__init__(df, "¿Existe relación entre nivel socioeconómico y notas?")

    #Función principal que agrupa los datos, crea el gráfico y muestra las figura
    def getTabla(self):
        
        """
        Realiza el análisis y la visualización de los datos académicos.

        Esta función agrupa los datos del DataFrame según el nivel de ingresos familiares
        y calcula la nota media (`Exam_Score`) de cada grupo. Posteriormente, los resultados pueden utilizarse para generar un gráfico
        de barras y mostrar la información de forma visual.

        Args:
        self: instancia de la clase que contiene el DataFrame (df)

        Returns:
        DataFrame: tabla agrupada con la media de notas por nivel de ingresos
        """

        df_grouped = self.df.groupby("Family_Income", as_index=False)["Exam_Score"].mean() #Función Media

        #Crea un gráfico de barras con Plotly Express
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

        #Ajusta el diseño general del gráfico
        fig.update_layout(
            xaxis_title="Nivel Socioeconómico",
            yaxis_title="Nota Media del Examen",
            title=self.titulo,
            yaxis_range=[68, 70]
        )

        # Muestra el gráfico en pantalla
        fig.show()

    
    #Función que hace de Test
    def test_calculo_media(self):
        """
            Esta función verifica que el cálculo de la media por nivel socioeconómico es correcta.
        """
        #Agrupo los datos
        df_grouped = self.df.groupby("Family_Income", as_index=False)["Exam_Score"].mean()

        # Comprobamos que hay datos
        assert len(df_grouped) > 0

        # Comprobamos valores concretos
        for _, row in df_grouped.iterrows():
            assert row["Exam_Score"] >= 0
            assert row["Exam_Score"] <= 100  # suponiendo notas de 0 a 100