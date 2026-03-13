import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="IA en Salud Mental",
    page_icon="🧠",
    layout="wide"
)

# Estilo personalizado: Fondo Lila, Títulos y Texto en Blanco
st.markdown("""
    <style>
    /* Fondo principal de la aplicación */
    .stApp {
        background-color: #C8A2C8; 
    }

    /* Color de todos los textos: títulos, párrafos, listas y etiquetas */
    h1, h2, h3, p, span, li, label, .stMarkdown {
        color: white !important;
    }

    /* Estilo para los bordes redondeados y contenedores */
    .stAlert, .stExpander, div[data-testid="stMetricValue"] {
        background-color: rgba(255, 255, 255, 0.15) !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 15px !important;
        color: white !important;
    }

    /* Ajuste para que el texto dentro de los expanders sea blanco */
    .streamlit-expanderHeader {
        color: white !important;
        background-color: transparent !important;
    }

    /* Líneas divisorias en blanco */
    hr {
        border-top: 1px solid rgba(255, 255, 255, 0.6) !important;
    }

    /* Estilo para la frase motivadora */
    .quote-text {
        text-align: left;
        font-style: italic;
        font-size: 1.1em;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Título y Frase Motivadora
st.title("¿Un psicólogo en el bolsillo?")
st.subheader("La revolución (y los riesgos) de la IA en nuestra salud mental")

st.markdown('<p class="quote-text">"La tecnología puede ser el puente, pero el encuentro entre dos seres humanos seguirá siendo el destino."</p>', unsafe_allow_html=True)
st.divider()

# 2. Cuerpo del Artículo: Introducción
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("En un mundo donde las citas con el psicólogo pueden tardar meses y los costos son prohibitivos, surge el chatbot de salud mental.")
        st.write("Para 2025, el uso más común de la IA generativa ya es la búsqueda de apoyo emocional.")
    with col2:
        st.info("**Pregunta clave:** ¿Es una solución real o un experimento digital a gran escala?")

# 3. Evolución (Tabs)
st.header("La metamorfosis del acompañante digital")
t1, t2, t3 = st.tabs(["Fase 1", "Fase 2", "Fase 3"])

with t1:
    st.write("**Guiones rígidos:** Sistemas de reglas que funcionaban como contestadores automáticos.")
with t2:
    st.write("**Machine Learning:** Los bots empezaron a entender el tono mediante procesamiento de lenguaje natural (NLP).")
with t3:
    st.write("**LLMs (Actualidad):** Sistemas como ChatGPT y Gemini que generan lenguaje nuevo y coherente en tiempo real.")

# 4. Evidencia Científica y Gráfico
st.header("¿Qué dice la ciencia?")
col_left, col_right = st.columns(2)

with col_left:
    # Datos para el gráfico
    data = {
        'Grupo': ['Universitarios (TCC)', 'Ansiedad General'],
        'Reducción de Síntomas': [22, 21]
    }
    df = pd.DataFrame(data)
    
    # Gráfico con colores que resaltan en el fondo lila
    fig = go.Figure(data=[
        go.Bar(x=df['Grupo'], y=df['Reducción de Síntomas'], marker_color='#FFFFFF', opacity=0.8)
    ])
