import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans


class ClusterAnalyzer:
    def run_kmeans(self, df):

        st.subheader("Clustering con K-Means")

        # Solo columnas numéricas
        numeric_df = df.select_dtypes(include=np.number)

        if numeric_df.shape[1] < 2:
            st.warning("Se necesitan al menos dos columnas numéricas para aplicar K-Means.")
            return df

        # Selección de número de clusters
        k = st.slider("Número de clusters (k)", 2, 10, 3)

        # Entrenar modelo
        model = KMeans(n_clusters=k, random_state=42)
        clusters = model.fit_predict(numeric_df)
        df['Cluster'] = clusters

        # Columnas a graficar
        x_col = st.selectbox("Selecciona la variable X", numeric_df.columns)
        y_col = st.selectbox("Selecciona la variable Y", numeric_df.columns)

        # Gráfico principal
        fig = px.scatter(
            numeric_df,
            x=x_col,
            y=y_col,
            color=df['Cluster'],
            title=f"Clustering K-Means: {x_col} vs {y_col}"
        )

        # Agregar centroides al gráfico
        centroids = model.cluster_centers_

        fig.add_trace(go.Scatter(
            x=centroids[:, numeric_df.columns.get_loc(x_col)],
            y=centroids[:, numeric_df.columns.get_loc(y_col)],
            mode="markers+text",
            marker=dict(size=14, symbol="x", color="black", line=dict(width=2)),
            text=[f"C{i}" for i in range(k)],
            textposition="top center",
            name="Centroides"
        ))

        st.plotly_chart(fig, width='stretch')

        # Tabla de centroides
        st.subheader("Tabla de centroides")
        centroid_df = pd.DataFrame(
            centroids,
            columns=numeric_df.columns
        )
        centroid_df.index = [f"Cluster {i}" for i in range(k)]

        st.dataframe(centroid_df.style.highlight_max(axis=0), width='stretch')

        # Interpretación automática de los clusters
        st.subheader("Interpretación automática de los clusters")

        for i in range(k):
            st.markdown(f"### 🔹 Cluster {i}")

            # punto central
            row = centroid_df.iloc[i]

            interpretation = []
            for col in numeric_df.columns:
                value = row[col]
                col_mean = numeric_df[col].mean()

                if value > col_mean:
                    interpretation.append(f"- Tiene **valores altos en `{col}`**.")
                elif value < col_mean:
                    interpretation.append(f"- Presenta **valores bajos en `{col}`**.")
                else:
                    interpretation.append(f"- `{col}` está en valores promedio.")

            block = "\n".join(interpretation)
            st.write(block)

        return df
