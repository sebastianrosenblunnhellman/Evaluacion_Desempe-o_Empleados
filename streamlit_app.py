# Importar librerías
import streamlit as st

# Crear página
st.set_page_config(page_title="Inicio", page_icon=":bar_chart:")  # Establecer el título y un icono para la página web

# Agregar un encabezado y un subencabezado a la página web
st.title("Evaluación del Desempeño de los Empleados")
st.subheader("📋 Instrucciones de las funcionalidades de la app")

# Instrucciones
st.write("""
En la aplicación desarrollada con Streamlit, hay dos secciones principales para monitorear el desempeño: una para repartidores y otra para armadores. Cada sección incluye las siguientes funcionalidades:

1. **🔍 Tres selectores**:
   - **👤 Nombre del empleado**: Permite filtrar los datos por el nombre del empleado.
   - **📅 Año**: Permite seleccionar el año de interés.
   - **📈 Métrica de desempeño**: Permite elegir la métrica de desempeño específica a analizar.

2. **📊 Gráfico de líneas (Line Chart)**: Visualiza la evolución de la métrica de desempeño seleccionada a lo largo del tiempo.

3. **📈 Indicador de progreso**: Muestra el progreso de la métrica seleccionada en relación con los objetivos establecidos.

Con el Indicador de progreso se calcula el porcentaje de diferencia entre la media anual y la media general, mostrando los puntos percentuales por debajo o por encima de cada métrica como un Indicador Clave de Desempeño (KPI).

Estas herramientas están diseñadas para proporcionar una visión clara y detallada del desempeño de los empleados, permitiendo identificar áreas de mejora y reconocer logros destacados.
""")
