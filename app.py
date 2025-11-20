import streamlit as st

# Importar clases de los módulos
from modulos.data_loader import DataLoader
from modulos.filters import DataFilter
from modulos.visualizations import Visualizer
from modulos.clustering import ClusterAnalyzer
from modulos.reports import ReportGenerator
from modulos.session_manager import SessionManager


def main():
    st.set_page_config(page_title="CSV/XLSX Analyzer Pro", layout="wide")
    st.title("Analizador Inteligente de Archivos CSV/XLSX")

    uploaded_file = st.file_uploader("Sube un archivo CSV o XLSX", type=['csv', 'xlsx'])

    if uploaded_file:
        # Cargar datos
        loader = DataLoader()
        df = loader.load(uploaded_file)
        df = df.convert_dtypes()
        df = df.astype({col: "string" for col in df.columns if df[col].dtype == "object"})


        if df is not None:
            # Aplicar filtros y limpiar datos
            filters = DataFilter()
            df = filters.apply_filters(df)
            df = filters.handle_missing_data(df)

            # Pestañas principales
            tabs = st.tabs(["Datos", "Resumen", "Gráficos", "Clustering"])

            # TAB 1 - Datos cargados
            with tabs[0]:
                st.subheader("Vista de datos cargados")
                n = st.number_input("Número de filas a mostrar", min_value=5, max_value=len(df), value=20)
                st.dataframe(df.head(n))


            # TAB 2 - Resumen estadístico
            with tabs[1]:
                st.subheader("Resumen Estadístico")
                st.write(df.describe(include='all'))

                st.markdown("---")

                # === Botón de Reporte PDF ===
                st.subheader("📄 Descargar Reporte PDF")
                report = ReportGenerator()
                report.create_pdf(df)

                st.markdown("---")

                # === Botón de guardar sesión (CSV) ===
                st.subheader("💾 Descargar Datos Filtrados (CSV)")
                session = SessionManager()
                session.save(df)

            # TAB 3 - Visualizaciones
            with tabs[2]:
                vis = Visualizer()
                vis.plot(df)

            # TAB 4 - Clustering con K-Means
            with tabs[3]:
                cluster = ClusterAnalyzer()
                df = cluster.run_kmeans(df)

    else:
        st.info("Por favor, carga un archivo CSV o XLSX para comenzar el análisis.")


if __name__ == "__main__":
    main()
