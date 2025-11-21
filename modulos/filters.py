import pandas as pd
import streamlit as st
import numpy as np

class DataFilter:
    def apply_filters(self, df):
        st.sidebar.subheader("Filtros de datos")
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                min_val, max_val = float(df[col].min()), float(df[col].max())
                selected = st.sidebar.slider(f"{col}", min_val, max_val, (min_val, max_val))
                df = df[df[col].between(selected[0], selected[1])]
            else:
                options = st.sidebar.multiselect(f"{col}", df[col].dropna().unique().tolist())
                if options:
                    df = df[df[col].isin(options)]
        st.sidebar.info(f"Filas después de filtrar: {df.shape[0]}")
        return df

    def handle_missing_data(self, df):
        st.subheader("Manejo de valores nulos")
        st.write(df.isnull().sum())
        action = st.radio("Selecciona una acción:", ["Ninguna", "Eliminar filas con nulos", "Rellenar con media/mediana"])
        if action == "Eliminar filas con nulos":
            df = df.dropna()
        elif action == "Rellenar con media/mediana":
            for col in df.select_dtypes(include=np.number).columns:
                df[col].fillna(df[col].mean(), inplace=True)
        return df