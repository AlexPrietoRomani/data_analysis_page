import streamlit as st
import pandas as pd
import plotly.express as px

def leer_archivo(archivo):
    """
    Lee un archivo Excel o CSV y devuelve un DataFrame.
    """
    if archivo.type in ["application/vnd.ms-excel", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
        return pd.read_excel(archivo, sheet_name='Nombre_de_la_hoja')
    elif archivo.type == "text/csv":
        return pd.read_csv(archivo)
    else:
        st.error("Formato de archivo no admitido. Por favor, sube un archivo Excel o CSV.")
        return None

def generar_boxplot(df, x_column, y_column):
  """
  Generates a boxplot for the specified columns of a DataFrame using Plotly.

  Args:
      df: The DataFrame with the data.
      x_column: The column for the x-axis.
      y_column: The column for the y-axis.

  Returns:
      A Plotly boxplot figure.
  """
  fig = px.box(data_frame=df, x=x_column, y=y_column)
  fig.update_layout(
      title=f"Boxplot: {y_column} vs {x_column}",
      xaxis_title=x_column,
      yaxis_title=y_column,
  )

  return fig

def generar_lineplot(df, x_column, y_column):
  """
  Generates a line plot for the specified columns of a DataFrame using Plotly.

  Args:
      df: The DataFrame with the data.
      x_column: The column for the x-axis.
      y_column: The column for the y-axis.

  Returns:
      A Plotly line plot figure.
  """
  fig = px.line(data_frame=df, x=x_column, y=y_column)
  fig.update_layout(
      title=f"Line Plot: {y_column} vs {x_column}",
      xaxis_title=x_column,
      yaxis_title=y_column,
  )

  return fig

def main():
    """
    La función principal de la aplicación.
    """

    # Título de la aplicación
    st.title("Análsisis de Data")

    # Cargar el archivo
    archivo = st.file_uploader("Subir archivo")
    if archivo is not None:
        # Leer el archivo
        df = leer_archivo(archivo)

        if df is not None:
            # Seleccionar las columnas para el gráfico
            columnas = st.multiselect("Seleccionar columnas", df.columns)

            # Verificar si hay al menos dos columnas seleccionadas
            if len(columnas) >= 2:
                # Configurar la selección de columnas para los ejes x e y
                x_column = st.selectbox("Seleccionar columna para el eje x", columnas)
                y_column = st.selectbox("Seleccionar columna para el eje y", columnas)

                # Display graph based on user input
                if st.button("Generate Boxplot"):
                    grafico = generar_boxplot(df, x_column, y_column)
                # Display graph based on user input
                if st.button("Generate Lineplot"):
                    grafico = generar_lineplot(df, x_column, y_column)

                # Mostrar el gráfico
                st.pyplot(grafico)
            else:
                st.warning("Selecciona al menos dos columnas para generar el gráfico boxplot.")

if __name__ == "__main__":
    main()

