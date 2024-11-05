import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

# Configuración de la aplicación
st.set_page_config(page_title="Aplicación Multiventana", layout="wide")

# Título de la aplicación
st.title("Bienvenido a la Aplicación Multiventana")

# Menú lateral con iconos
st.sidebar.title("Menú")
page = st.sidebar.selectbox("Selecciona una opción:", ["🏠 Inicio", "📊 Visualización de Datos", "📈 Gráficos Interactivos"])

# Lógica para cada sección
if page == "🏠 Inicio":
    st.write("¡Hola! Esta es una aplicación multiventana construida con Streamlit.")
    st.write("Utiliza el menú en la barra lateral para navegar entre las diferentes secciones.")
    
elif page == "📊 Visualización de Datos":
    st.title("Visualización de Datos")
    st.markdown("""
    Esta sección te permite cargar un archivo CSV y visualizar su contenido.
    Asegúrate de que el archivo tenga un formato adecuado.
    """)
    
    uploaded_file = st.file_uploader("Cargar un archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("Datos cargados correctamente.")
            st.dataframe(df)

            # Convertir el DataFrame a un archivo Excel en memoria
            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)  # Volver al inicio del buffer

            # Botón para descargar el DataFrame como Excel
            if st.download_button(
                label="Descargar como Excel",
                data=excel_buffer,
                file_name='datos_visualizacion.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            ):
                st.success("¡Archivo descargado!")
        except Exception as e:
            st.error(f"Error al cargar el archivo: {e}")
    
elif page == "📈 Gráficos Interactivos":
    st.title("Gráficos Interactivos")
    
    uploaded_file = st.file_uploader("Cargar un archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("Datos cargados correctamente.")
            st.dataframe(df)

            # Selección de ejes para el gráfico
            columnas = df.columns.tolist()
            eje_x = st.selectbox("Selecciona el eje X:", columnas)
            eje_y = st.selectbox("Selecciona el eje Y:", columnas)
            tipo_grafico = st.selectbox("Selecciona el tipo de gráfico:", ["Línea", "Barras"])

            if st.button("Crear Gráfico"):
                plt.figure(figsize=(10, 5))
                if tipo_grafico == "Línea":
                    plt.plot(df[eje_x], df[eje_y])
                elif tipo_grafico == "Barras":
                    plt.bar(df[eje_x], df[eje_y])
                
                plt.title(f'Gráfico de {eje_y} vs {eje_x}')
                plt.xlabel(eje_x)
                plt.ylabel(eje_y)
                st.pyplot(plt)

            # Convertir el DataFrame a un archivo Excel en memoria
            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, engine='openpyxl')
            excel_buffer.seek(0)  # Volver al inicio del buffer

            # Botón para descargar el DataFrame como Excel
            if st.download_button(
                label="Descargar como Excel",
                data=excel_buffer,
                file_name='datos_graficos.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            ):
                st.success("¡Archivo descargado!")
                
        except Exception as e:
            st.error(f"Error al cargar el archivo: {e}")