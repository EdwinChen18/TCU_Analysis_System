import streamlit as st
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans

class ClusterAnalyzer:
    def run_kmeans(self, df):
        st.subheader("Clustering con K-Means")
        numeric_df = df.select_dtypes(include=np.number)
        if numeric_df.shape[1] < 2:
            st.warning("Se necesitan al menos dos columnas numéricas para aplicar K-Means.")
            return df

        k = st.slider("Número de clusters (k)", 2, 10, 3)
        model = KMeans(n_clusters=k, random_state=42)
        clusters = model.fit_predict(numeric_df)
        df['Cluster'] = clusters

        x_col = st.selectbox("Selecciona la variable X", numeric_df.columns)
        y_col = st.selectbox("Selecciona la variable Y", numeric_df.columns)

        fig = px.scatter(
            numeric_df, x=x_col, y=y_col, color=df['Cluster'],
            title=f"Clustering K-Means: {x_col} vs {y_col}"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        return df
