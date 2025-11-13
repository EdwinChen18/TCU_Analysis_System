# TCU_Analysis_System
Trabajo Comunal Universitario – Universidad Fidélitas
Aplicación web desarrollada en Streamlit para analizar, visualizar y exportar datos desde archivos CSV o XLSX, con funciones de filtrado dinámico, clustering con K-Means y generación automática de reportes PDF.

# Analizador Inteligente de Archivos CSV/XLSX

Este proyecto fue desarrollado como parte del Trabajo Comunal Universitario (TCU) de la carrera de Ingeniería en Sistemas de Computación en la Universidad Fidélitas.

Su propósito es ofrecer una herramienta accesible que facilite a instituciones educativas públicas el análisis de información académica y administrativa mediante la carga de archivos CSV o Excel, permitiendo obtener reportes automáticos, visualizaciones interactivas y agrupamientos de datos con inteligencia artificial.

## Funcionalidades principales
- Carga de archivos CSV o XLSX.  
- Filtros dinámicos para explorar subconjuntos de datos.  
- Visualizaciones interactivas (dispersión, barras, líneas, histogramas).  
- Clustering automático con algoritmo **K-Means**.  
- Limpieza y manejo de valores nulos.  
- Generación automática de reportes PDF.  
- Guardado de sesión y exportación de resultados.

## Instalación

1. Clonar el repositorio o descargar los archivos del proyecto:

git clone https://github.com/tu_usuario/TCU_Analysis_System.git
cd TCU_Analysis_System


2. Crear y activar un entorno virtual:

python -m venv .venv
.venv\Scripts\activate       # En Windows
source .venv/bin/activate    # En Linux o Mac


3. Instalar las dependencias:

pip install -r requirements.txt

## Uso

1. Ejecute la aplicación:

```bash
streamlit.cmd run .\app.py
```
2. Abra su navegador web y vaya a la URL que se muestra en la terminal (normalmente http://localhost:8501).
3. Cargue su archivo CSV/XLSX utilizando el cargador de archivos.
4. Explore las distintas pestañas de análisis para obtener información valiosa a partir de sus datos.


## Requisitos del sistema

- Python 3.8 o superior
- Streamlit 1.25.0 o superior
- Pandas 2.0.0 o superior
- NumPy 1.24.0 o superior
- Plotly 5.15.0 o superior
- scikit-learn 1.3.0 o superior
- FPDF o ReportLab para generación de reportes PDF

Todas las dependencias necesarias están especificadas en el archivo requirements.txt
