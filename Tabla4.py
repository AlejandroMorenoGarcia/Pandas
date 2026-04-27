import plotly.express as px
from Tablas import Tablas

class TablaAxel(Tablas):
    def __init__(self, df):
        super().__init__(df, "¿El acceso a recursos e internet marca diferencias relevantes?")

    def getTabla(self):
        tabla = self.df.groupby("Internet_Access")["Exam_Score"].mean().round(2).reset_index()
        tabla.columns = ["Acceso a Internet", "Nota Media"]
        tabla["Acceso a Internet"] = tabla["Acceso a Internet"].replace({"Yes": "Sí", "No": "No"})

        print(tabla.to_string(index=False))

        fig = px.bar(
            tabla,
            x="Acceso a Internet",
            y="Nota Media",
            color="Acceso a Internet",
            text="Nota Media",
            title="Nota media según acceso a internet",
            template="plotly_dark"
        )

        fig.update_yaxes(range=[66, 68])
        fig.show(renderer="browser") 
