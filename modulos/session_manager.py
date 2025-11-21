import streamlit as st


class SessionManager:
    def save(self, df):
        csv_data = df.to_csv(index=False).encode('utf-8')
        st.download_button("Descargar sesión CSV", csv_data, file_name="analisis_actual.csv", mime="text/csv")