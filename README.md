# 🚀 Evaluación de Desempeño Empleados 📊

El objetivo final de este proyecto es desarrollar una aplicación analítica para evaluar el desempeño de los empleados en una pequeña empresa de envíos. 📦 Debido a razones de privacidad, el set de datos original y la identidad de la empresa han sido resguardados. Lo que queda aquí expuesto es la estructura del proyecto y la secuencia resolutiva que se trazó en el mismo.

[![Ver Demo](https://img.shields.io/badge/Demo-Visitar%20Demo-brightgreen)](https://empleadoss.streamlit.app)


# 🏢 Descripción de la Empresa
La empresa está dividida en dos roles principales: **armadores** y **repartidores**.
Los armadores 🔧 son responsables de preparar cada pedido, buscando los productos en el depósito, sellando la caja con la dirección de entrega y dejándola lista para los repartidores. Los repartidores 🚚 transportan los pedidos hasta el domicilio de los respectivos clientes.

## 🎯 Objetivos empresariales
- Obtener un registro y seguimiento de los datos más relevantes para analizar el desempeño de los empleados.
- Establecer indicadores claves de rendimiento pertinentes para el monitoreo y la toma de decisiones en función de dichos datos.

## 📖 Diccionario de datos
Se obtuvieron una gran cantidad de datos de interés por parte del sector de recursos humanos de la empresa. Otras variables de interés se obtuvieron mediante la aplicación de cuestionarios ad hoc.

## 🛵 Repartidores

### 📈 Desempeño

<table>
  <tr>
    <th>Variable</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td>id_empleado</td>
    <td>Número de identificación del empleado.</td>
  </tr>
  <tr>
    <td>Nombre</td>
    <td>Nombre del empleado.</td>
  </tr>
  <tr>
    <td>tarde</td>
    <td>Número de veces que el repartidor llega tarde al trabajo en el mes.</td>
  </tr>
  <tr>
    <td>faltas</td>
    <td>Número de ausencias no justificadas en el mes.</td>
  </tr>
  <tr>
    <td>asignados</td>
    <td>Número de pedidos asignados en el mes.</td>
  </tr>
  <tr>
    <td>completados</td>
    <td>Número de pedidos completados en el mes.</td>
  </tr>
  <tr>
    <td>horas_extra</td>
    <td>Cantidad de horas extra trabajadas en el mes.</td>
  </tr>
  <tr>
    <td>satisfaccion_cliente</td>
    <td>Puntajes de satisfacción del cliente basados en encuestas post-entrega (promedio mensual).</td>
  </tr>
  <tr>
    <td>jornada</td>
    <td>Cantidad de horas trabajadas al día (promedio mensual).</td>
  </tr>
  <tr>
    <td>km_recorridos</td>
    <td>Cantidad de kilómetros recorridos en el mes.</td>
  </tr>
  <tr>
    <td>fecha</td>
    <td>Mes y año de subida de la información.</td>
  </tr>
</table>

### 🧑‍🤝‍🧑 Comportamiento

<table>
  <tr>
    <th>Variable</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td>grupal</td>
    <td>Evaluaciones de compañeros sobre la capacidad del empleado para trabajar en equipo.</td>
  </tr>
  <tr>
    <td>individual</td>
    <td>Evaluación del empleado sobre su propia satisfacción en el ambiente laboral.</td>
  </tr>
</table>

## 🔧 Armadores

### 📈 Desempeño

<table>
  <tr>
    <th>Variable</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td>id_empleado</td>
    <td>Número de identificación del empleado.</td>
  </tr>
  <tr>
    <td>Nombre</td>
    <td>Nombre del empleado.</td>
  </tr>
  <tr>
    <td>tarde</td>
    <td>Número de veces que el armador llega tarde al trabajo.</td>
  </tr>
  <tr>
    <td>faltas</td>
    <td>Número de ausencias no justificadas.</td>
  </tr>
  <tr>
    <td>asignados</td>
    <td>Número de pedidos asignados por hora.</td>
  </tr>
  <tr>
    <td>completados</td>
    <td>Número de pedidos armados por hora.</td>
  </tr>
  <tr>
    <td>horas_extra</td>
    <td>Cantidad de horas extra trabajadas.</td>
  </tr>
  <tr>
    <td>errores_armado</td>
    <td>Número de pedidos con errores en el armado (devueltos o reclamados).</td>
  </tr>
  <tr>
    <td>tiempo_descanso</td>
    <td>Registro de tiempos de descanso y pausas durante la jornada laboral.</td>
  </tr>
  <tr>
    <td>fecha</td>
    <td>Mes y año de subida de la información.</td>
  </tr>
</table>

### 🧑‍🤝‍🧑 Comportamiento

<table>
  <tr>
    <th>Variable</th>
    <th>Descripción</th>
  </tr>
  <tr>
    <td>grupal</td>
    <td>Evaluaciones de compañeros sobre la capacidad del empleado para trabajar en equipo.</td>
  </tr>
  <tr>
    <td>individual</td>
    <td>Evaluación del empleado sobre su propia satisfacción en el ambiente laboral.</td>
  </tr>
</table>

### 🛠️ Desarrollo

Los empleados de recursos humanos se encargan de rellenar las plantillas necesarias en formato spreadsheet una vez por mes. Dicho Google Sheets alojado en Google Drive alimenta directamente al dashboard de Streamlit. Para añadir valor y profundidad a las Variables de Desempeño que proveía el sector de recursos humanos, planteamos la necesidad de recabar información de Variables Comportamentales a través de cuestionarios ad hoc. Los mismos permiten matizar los datos cruzando dos variables relacionadas.

En la aplicación desarrollada con Streamlit hay una seccion para monitorear a repartidores y otra para armadores. Cada una contiene tres selectores y un line chart, ademas de un indicador de progreso. Los selectores filtran los datos por nombre del empleado, año y métrica de desempeño. Ademas se calcula el porcentaje de diferencia entre la media anual y la media general y se muestra los puntos percentuales por debajo o por encima para cada metrica a modo de indicador clave de desempeño (KPI).