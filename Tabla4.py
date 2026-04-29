import plotly.express as px
from Tablas import Tablas

class Tabla4(Tablas):
    def __init__(self, df):
        super().__init__(df, "¿El acceso a recursos e internet marca diferencias relevantes?")

    def getTabla(self):
        color_discrete_map = {
            "Yes": "#ADFF2F",  # verde lima
            "No": "#FF073A",  # rojo neón
        }

        tabla = self.df.groupby("Internet_Access")["Exam_Score"].mean().round(2).reset_index()
        tabla.columns = ["Acceso a Internet", "Nota Media"]
        tabla["Acceso a Internet"] = tabla["Acceso a Internet"].replace({"Yes": "Sí", "No": "No"})

        print(tabla.to_string(index=False))

        fig = px.bar(
            tabla,
            x="Acceso a Internet",
            y="Nota Media",
            color="Acceso a Internet",
            color_discrete_map= color_discrete_map,
            text="Nota Media",
            title=self.titulo,
            template="plotly_dark"
        )

        fig.update_yaxes(range=[68, 69.5])
        fig.show()
