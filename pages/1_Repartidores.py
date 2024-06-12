import streamlit as st
import pandas as pd
import altair as alt

# Configurar la página
st.set_page_config(page_title="Repartidores", page_icon="🔥", layout="wide")

# Encabezado
st.header("Control de desempeño en Armadores")

# Línea divisoria
st.markdown("---")

# Cargar los datos
path = r"./data/repartidores/repartidores.csv"
data = pd.read_csv(path)
df = pd.DataFrame(data)

# Convertir la columna 'fecha' a tipo datetime y extraer el año y mes
df['fecha'] = pd.to_datetime(df['fecha'])
df['año'] = df['fecha'].dt.year
df['mes'] = df['fecha'].dt.month

# Configuración de la interfaz de usuario
st.title("Dashboard de Empleados")

# Filtros
nombre = st.selectbox("Seleccionar Nombre", df['nombre'].unique())
año = st.selectbox("Seleccionar Año", df['año'].unique())
metricas = {
    "Faltas (sin justificar)": "faltas",
    "LLegadas tarde": "tarde",
    "Pedidos completados": "completados",
    "Horas Extra": "horas_extra",
    "Satisfacción del Cliente": "satisfaccion_cliente",
    "Satisfacción en ambiente laboral": "Score satisfacción laboral",
    "Score Trabajo en Equipo": "Score trabajo en equipo"
}
metrica = st.selectbox("Seleccionar Métrica", list(metricas.keys()))

# Filtrar el DataFrame según los filtros seleccionados
df_filtered = df[(df['nombre'] == nombre) & (df['año'] == año)]

# Calcular la media anual de la métrica seleccionada
media_anual = df_filtered[metricas[metrica]].mean()

# Calcular la media general de la métrica seleccionada
media_general = df[metricas[metrica]].mean()

# Calcular el porcentaje por encima o por debajo de la media
porcentaje = ((media_anual - media_general) / media_general) * 100

# Mostrar el KPI
if porcentaje > 0:
    st.metric(label=f"{metrica} vs Media General", value=f"{media_anual:.2f}", delta=f"{porcentaje:.2f}% por encima de la media")
else:
    st.metric(label=f"{metrica} vs Media General", value=f"{media_anual:.2f}", delta=f"{porcentaje:.2f}% por debajo de la media")

# Crear un gráfico de líneas
line_chart = alt.Chart(df_filtered).mark_line().encode(
    x=alt.X('mes:O', title='Mes'),
    y=alt.Y(f'{metricas[metrica]}:Q', title=metrica),
    tooltip=['mes', metricas[metrica]]
).properties(
    title=f'{metrica} por Mes para {nombre} en {año}',
    width=700,
    height=400
)

# Mostrar el gráfico en la app de Streamlit
st.altair_chart(line_chart, use_container_width=True)
