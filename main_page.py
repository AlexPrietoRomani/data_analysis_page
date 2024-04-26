import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

def generar_boxplot(df, x_column, y_column, z_column):
    """
    Genera un gráfico boxplot para las columnas especificadas de un DataFrame.

    Args:
        df: El DataFrame con los datos.
        x_column: La columna para el eje x.
        y_column: La columna para el eje y.
        z_column: La columna para el filtro.

    Returns:
        Un gráfico boxplot.
    """
    #valor de z_columna poner como default en None
    z_columna = None
    
    #Cambiar valor de z_columna si existe una selección de el 4to parametro
    if z_columna is None:
        z_columna = z_column
    
    #Creando condicial si existe valor de z_column
    if z_columna is None:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=df[x_column], y=df[y_column], palette= "hls")
        plt.title(f"Gráfico boxplot: {y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
    if z_column is not None:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x=df[x_column], y=df[y_column], palette= "hls", hue= df[z_column])
        plt.title(f"Gráfico boxplot: {y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
    return plt

def generar_lineplot(df, x_column, y_column, z_column):
    """
    Genera un gráfico boxplot para las columnas especificadas de un DataFrame.

  Args:
      df: The DataFrame with the data.
      x_column: The column for the x-axis.
      y_column: The column for the y-axis.

    Returns:
        Un gráfico boxplot.
    """
    #valor de z_columna poner como default en None
    z_columna = None
    
    #Cambiar valor de z_columna si existe una selección de el 4to parametro
    if z_columna is None:
        z_columna = z_column
    
    #Creando condicial si existe valor de z_column
    if z_columna is None:
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x=df[x_column], y=df[y_column], palette= "hls")
        plt.title(f"Gráfico boxplot: {y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
    if z_columna is not None:
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x=df[x_column], y=df[y_column], palette= "hls", hue= df[z_columna])
        plt.title(f"Gráfico boxplot: {y_column} vs {x_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid()
    return plt

def generar_boxplot_suma_acumulado(df, x_column, y_column, z_column):
    """
    Genera un gráfico boxplot para las columnas especificadas de un DataFrame.

    Args:
        df: El DataFrame con los datos.
        x_column: La columna para el eje x.
        y_column: La columna para el eje y.
        z_column: La columna para agrupar por repetición.

    Returns:
        Un gráfico boxplot.
    """
    #Sumanos la agrupaciones de los Kg
    df = df.groupby([x_column,z_column])[y_column].sum().reset_index()
    # Convertir la columna 'Plot' a categórica
    df[x_column] = df[x_column].astype(str)    
    df[x_column] = pd.Categorical(df[x_column])
    # Creamos un objeto Figure
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=df[x_column], y=df[y_column], palette= "hls")
    plt.title(f"Gráfico boxplot: {y_column} vs {x_column} Acumulate")
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
                z_column = st.selectbox("Seleccionar columna para filtro o columna de repetición", columnas, index = None)
                
                
                st.markdown(f"{z_column}")

                if st.button("Generate Boxplot"):
                    grafico = generar_boxplot(df, x_column, y_column, z_column)
                # Display graph based on user input
                if st.button("Generate Lineplot"):
                    grafico = generar_lineplot(df, x_column, y_column, z_column)
                if st.button("Generate Boxplot Acumulate"):
                    grafico = generar_boxplot_suma_acumulado(df, x_column, y_column, z_column)
                # Mostrar el gráfico
                st.pyplot(grafico)
            else:
                st.warning("Selecciona al menos dos columnas para generar el gráfico boxplot.")

if __name__ == "__main__":
    main()

