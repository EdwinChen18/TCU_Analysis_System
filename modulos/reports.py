import streamlit as st
from fpdf import FPDF
import io
import pandas as pd


# Truncar texto dentro de celdas 
def fit_text(text, max_chars=10):
    text = str(text)
    return text if len(text) <= max_chars else text[:max_chars] + "..."


# Sanitizar texto para evitar errores de unicode 
def sanitize(text):
    return str(text).encode("latin-1", "replace").decode("latin-1")


class ReportGenerator:
    def create_pdf(self, df):

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)

        # Portada
        pdf.add_page()

        try:
            pdf.image("documentos/logo.png", x=10, y=8, w=40)
        except:
            pass

        pdf.set_xy(150, 8)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(
            50, 5,
            sanitize(
                "Escuela Barrio del Socorro\n"
                "esc.barrio.del.socorro@mep.go.cr\n"
                "+506 2100-5295\n"
                "Heredia, Costa Rica"
            ),
            align="R"
        )

        # Título  centrado 
        pdf.set_font("Arial", "B", 20)

        title = "Reporte de Análisis de Datos"

        # Cálculo del ancho del texto
        title_width = pdf.get_string_width(title) + 6

        # Ancho disponible entre las dos columnas
        left_limit = 10 + 40 + 10      # logo_x + logo_width + margen
        right_limit = 150 - 10         # x donde empieza info institucional 
        available_width = right_limit - left_limit

        # Coordenada X para centrar el título
        title_x = left_limit + (available_width - title_width) / 2

        pdf.set_xy(title_x, 25)
        pdf.cell(title_width, 10, sanitize(title), ln=True, align="C")

        pdf.ln(15)

        # Resumen General

        pdf.set_font("Arial", "B", 14)
        pdf.cell(0, 10, sanitize("Resumen General del Dataset"), ln=True)

        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 8, sanitize(f"Total de filas: {df.shape[0]}"))
        pdf.multi_cell(0, 8, sanitize(f"Total de columnas: {df.shape[1]}"))
        pdf.ln(5)

        # Tabla Estadísticas

        # Redondear estadísticas
        stats = df.describe(include="all")
        stats = stats.astype("string").fillna("")
        for col in stats.columns:
            stats[col] = stats[col].map(lambda x: f"{x:.2f}" if isinstance(x, (int, float)) else x)

        # Página en horizontal
        pdf.add_page(orientation="L")

        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, sanitize("Estadísticas Generales"), ln=True)

        pdf.ln(3)
        pdf.set_font("Arial", size=8)

        # Ajustar ancho de columna
        col_width = pdf.w / (len(stats.columns) + 1)

        # Encabezados
        pdf.set_font("Arial", "B", 8)
        pdf.cell(col_width, 8, sanitize("Estadística"), 1)

        for col in stats.columns:
            pdf.cell(col_width, 8, sanitize(fit_text(col, 10)), 1)
        pdf.ln()

        # Filas 
        pdf.set_font("Arial", size=7)

        for idx, row in stats.iterrows():
            pdf.cell(col_width, 8, sanitize(fit_text(idx, 10)), 1)
            for value in row:
                pdf.cell(col_width, 8, sanitize(fit_text(value, 10)), 1)
            pdf.ln()

        # Exportar PDF
        pdf_bytes = pdf.output(dest="S").encode("latin-1", "replace")

        st.download_button(
            "Descargar Reporte PDF Profesional",
            data=pdf_bytes,
            file_name="reporte_analisis.pdf",
            mime="application/pdf")
