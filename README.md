# Evaluación del Desempeño de los Empleados

El objetivo final de este proyecto es desarrollar una aplicación analítica para evaluar el desempeño de los empleados en una pequeña empresa de envíos. Debido a razones de privacidad, el set de datos original y la identidad de la empresa han sido resguardados. Lo que queda aquí expuesto es la estructura del proyecto y la secuencia resolutiva que se trazó en el mismo.

# Descripción de la Empresa
La empresa está dividida en dos roles principales: armadores y repartidores.
Los armadores son responsables de preparar cada pedido, buscando los productos en el depósito, sellando la caja con la dirección de entrega y dejándola lista para los repartidores. Los repartidores transportan los pedidos hasta el domicilio de los respectivos clientes. 

## Objetivos empresariales
- Obtener un registro y seguimiento de los datos más relevantes para analizar el desempeño de los empleados.
- Establecer indicadores claves de rendimiento pertinentes para el monitoreo y la toma de decisiones en función de dichos datos.

## Diccionario de datos
Se obtuvieron una gran cantidad de datos de interés por parte del sector de recursos humanos de la empresa. Otras variables de interés se obtuvieron mediante la aplicación de cuestionarios ad hoc.

## Variables para Repartidores

### Desempeño
- **id_empleado**: Número de identificación del empleado.
- **Nombre**: Nombre del empleado.
- **tarde**: Número de veces que el repartidor llega tarde al trabajo en el mes.
- **faltas**: Número de ausencias no justificadas en el mes.
- **asignados**: Número de pedidos asignados en el mes.
- **completados**: Número de pedidos completados en el mes.
- **horas_extra**: Cantidad de horas extra trabajadas en el mes.
- **satisfaccion_cliente**: Puntajes de satisfacción del cliente basados en encuestas post-entrega (promedio mensual).
- **jornada**: Cantidad de horas trabajadas al día (promedio mensual).
- **km_recorridos**: Cantidad de kilómetros recorridos en el mes.
- **fecha**: Mes y año de subida de la información.

### Variables Comportamentales
- **grupal**: Evaluaciones de compañeros sobre la capacidad del empleado para trabajar en equipo.
- **individual**: Evaluación del empleado sobre su propia satisfacción en el ambiente laboral.

## Armadores

### Variables de Desempeño
- **id_empleado**: Número de identificación del empleado.
- **Nombre**: Nombre del empleado.
- **tarde**: Número de veces que el armador llega tarde al trabajo.
- **faltas**: Número de ausencias no justificadas.
- **asignados**: Número de pedidos asignados por hora.
- **completados**: Número de pedidos armados por hora.
- **horas_extra**: Cantidad de horas extra trabajadas.
- **errores_armado**: Número de pedidos con errores en el armado (devueltos o reclamados).
- **tiempo_descanso**: Registro de tiempos de descanso y pausas durante la jornada laboral.
- **fecha**: Mes y año de subida de la información.

### Variables Comportamentales
- **grupal**: Evaluaciones de compañeros sobre la capacidad del empleado para trabajar en equipo.
- **individual**: Evaluación del empleado sobre su propia satisfacción en el ambiente laboral.

### Desarrollo

Los empleados de recursos humanos se encargan de rellenar las plantillas necesarias en formato spreadsheet una vez por mes. Dicho Google Sheets alojado en Google Drive alimenta directamente al dashboard de Streamlit. Para añadir valor y profundidad a las Variables de Desempeño que proveía el sector de recursos humanos, planteamos la necesidad de recabar información de Variables Comportamentales a través de cuestionarios ad hoc. Los mismos permiten matizar los datos cruzando dos variables relacionadas.

En la aplicación desarrollada con Streamlit, se realiza lo siguiente:

1. **Configuración de la página**: Se establece el título, el ícono y el diseño de la página.
2. **Carga y preparación de datos**: Se cargan los datos desde un archivo CSV, se convierten las fechas al tipo `datetime` y se extraen los años y meses.
3. **Configuración de la interfaz de usuario**: Se establece el título del dashboard y se crean selectores para filtrar los datos por nombre, año y métrica de desempeño.
4. **Filtrado y cálculo de métricas**: Se filtra el DataFrame según el nombre y el año seleccionados, se calculan la media anual de la métrica seleccionada y la media general, y se calcula el porcentaje de diferencia entre la media anual y la media general.
5. **Visualización de KPI**: Se muestra un indicador clave de desempeño (KPI) con la comparación de la métrica seleccionada respecto a la media general.
6. **Creación y visualización de gráficos**: Se crea un gráfico de líneas con Altair para visualizar la métrica seleccionada por mes y se muestra en la aplicación de Streamlit.

Este enfoque permite a los usuarios filtrar y visualizar el desempeño de los empleados en función de diferentes métricas y compararlas con la media general, proporcionando una vista detallada y gráfica del rendimiento a lo largo del tiempo.
