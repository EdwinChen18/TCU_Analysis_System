import pandas as pd
import streamlit as st


class DataLoader:
    def load(self, uploaded_file):
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                raise ValueError("Formato no soportado. Solo se permiten CSV o XLSX.")
            return df
        except Exception as e:
            st.error(f"Error al cargar el archivo: {e}")
            return None