import plotly.express as px
from Tablas import Tablas

class Tabla4(Tablas):
    def __init__(self, df):
        # Llama al constructor de la clase padre (Tablas)
        # define el título de la gráfica
        super().__init__(df, "¿El acceso a recursos e internet marca diferencias relevantes?")

    def getTabla(self):
        """
        Hace una tabla y una gráfica de barras, analiza la relación entre
        el acceso a internet y nota media de los estudiantes.

        - Agrupa los datos por acceso a internet (en "Yes/No").
        - Calcula la (Exam_Score) para cada grupo.
        - Imprime el resultado en tabla en la consola.
        - Crea la gráfica de barras con Plotly para ver mejor la diferencia,
        y podemos ajustar el rango del eje Y para ver algún detalle.
        """
        # Asignamos colores a las dos categorías
        color_discrete_map = {
            "Yes": "#ADFF2F",  # verde lima
            "No": "#FF073A",  # rojo neón
        }
        
        # Agrupa los datos por acceso a internet y calcula la media de las notas.
        tabla = self.df.groupby("Internet_Access")["Exam_Score"].mean().round(2).reset_index()
        
        # Cambia el nombre a español para que se pueda entender mejor.
        tabla.columns = ["Acceso a Internet", "Nota Media"]
        
        # Traduce los valores a "SI / NO".
        tabla["Acceso a Internet"] = tabla["Acceso a Internet"].replace({"Yes": "Sí", "No": "No"})

        # Imprime la tabla en la consola sin mostrar el índice
        print(tabla.to_string(index=False))

        # gráfica de barras con Plotly
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
        # Ajusta el rango del eje Y para poder ver mejor la diferencia
        fig.update_yaxes(range=[68, 69.5])
        
        # Muestra la gráfica.
        fig.show()
