import streamlit as st
import pandas as pd

# Importar clases de los módulos
from modules.data_loader import DataLoader
from modules.filters import DataFilter
from modules.visualizations import Visualizer
from modules.clustering import ClusterAnalyzer
from modules.reports import ReportGenerator
from modules.session_manager import SessionManager


def main():
    st.set_page_config(page_title="CSV/XLSX Analyzer Pro", layout="wide")
    st.title("Analizador Inteligente de Archivos CSV/XLSX")

    uploaded_file = st.file_uploader("Sube un archivo CSV o XLSX", type=['csv', 'xlsx'])

    if uploaded_file:
        # Cargar datos
        loader = DataLoader()
        df = loader.load(uploaded_file)

        if df is not None:
            # Aplicar filtros y limpiar datos
            filters = DataFilter()
            df = filters.apply_filters(df)
            df = filters.handle_missing_data(df)

            # Pestañas principales
            tabs = st.tabs(["Datos", "Resumen", "Gráficos", "Clustering", "Reporte", "Sesión"])

            # TAB 1 - Datos cargados
            with tabs[0]:
                st.subheader("Vista de datos cargados")
                st.dataframe(df.head())

            # TAB 2 - Resumen estadístico
            with tabs[1]:
                st.subheader("Resumen Estadístico")
                st.write(df.describe(include='all'))

            # TAB 3 - Visualizaciones
            with tabs[2]:
                vis = Visualizer()
                vis.plot(df)

            # TAB 4 - Clustering con K-Means
            with tabs[3]:
                cluster = ClusterAnalyzer()
                df = cluster.run_kmeans(df)

            # TAB 5 - Generar reporte PDF
            with tabs[4]:
                report = ReportGenerator()
                report.create_pdf(df)

            # TAB 6 - Guardar sesión
            with tabs[5]:
                session = SessionManager()
                session.save(df)
    else:
        st.info("Por favor, carga un archivo CSV o XLSX para comenzar el análisis.")


if __name__ == "__main__":
    main()
