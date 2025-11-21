import plotly.express as px
import streamlit as st
import numpy as np
import io

class Visualizer:
    def plot(self, df):
        st.subheader("Visualizaciones")
        numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

        if numeric_cols:
            x_col = st.selectbox("Variable X", numeric_cols)
            y_col = st.selectbox("Variable Y", numeric_cols)
            chart_type = st.selectbox("Tipo de gráfico", ["Dispersión", "Barras", "Líneas", "Histograma"])

            if chart_type == "Dispersión":
                fig = px.scatter(df, x=x_col, y=y_col, title=f"Dispersión: {x_col} vs {y_col}")
            elif chart_type == "Barras":
                fig = px.bar(df, x=x_col, y=y_col, title=f"Barras: {x_col} vs {y_col}")
            elif chart_type == "Líneas":
                fig = px.line(df, x=x_col, y=y_col, title=f"Líneas: {x_col} vs {y_col}")
            else:
                fig = px.histogram(df, x=x_col, title=f"Histograma: {x_col}")

            st.plotly_chart(fig, width='stretch')

        else:
            st.warning("No se encontraron columnas numéricas para graficar.")