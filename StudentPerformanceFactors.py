import pandas as pd
import plotly.express as px

df = pd.read_csv('StudentPerformanceFactors.csv')

print(df.columns) 

color_discrete_map = {
    "Male": "#2979FF",    # azul eléctrico
    "Female": "#FF1744"   # rojo/rosa intenso
}

df_largo = df.groupby(["Hours_Studied", "Exam_Score", "Gender","Attendance"]).size().reset_index(name="Count")

print(df_largo)

fig = px.scatter_3d(df_largo, x="Hours_Studied", y="Attendance", z="Exam_Score", color="Gender", color_discrete_map=color_discrete_map, size="Count", template="plotly_dark", size_max=30)
fig.update_traces(marker=dict(
    line=dict(
        width=0,
        color="black"
    )
))
fig.show(renderer="browser")

print(df_largo.head())
print(df_largo["Hours_Studied"].nunique())
print(df_largo.dtypes)