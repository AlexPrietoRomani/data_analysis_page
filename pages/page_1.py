import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

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
    Genera un gráfico boxplot para las columnas especificadas de un DataFrame.

    Args:
        df: El DataFrame con los datos.
        x_column: La columna para el eje x.
        y_column: La columna para el eje y.

    Returns:
        Un gráfico boxplot.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=df[x_column], y=df[y_column], palette= "hls")
    plt.title(f"Gráfico boxplot: {y_column} vs {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid()
    return plt

def generar_lineplot(df, x_column, y_column):
    """
    Genera un gráfico boxplot para las columnas especificadas de un DataFrame.

    Args:
        df: El DataFrame con los datos.
        x_column: La columna para el eje x.
        y_column: La columna para el eje y.

    Returns:
        Un gráfico boxplot.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=df[x_column], y=df[y_column], palette= "hls")
    plt.title(f"Gráfico boxplot: {y_column} vs {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid()
    return plt

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

