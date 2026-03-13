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
st.title("¿Un psicólogo en el bolsillo? [cite: 1, 2]")
st.subheader("La revolución (y los riesgos) de la IA en nuestra salud mental [cite: 2]")

st.markdown('<p class="quote-text">"La tecnología puede ser el puente, pero el encuentro entre dos seres humanos seguirá siendo el destino." [cite: 3]</p>', unsafe_allow_html=True)
st.divider()

# 2. Cuerpo del Artículo: Introducción
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("En un mundo donde las citas con el psicólogo pueden tardar meses y los costos son prohibitivos, surge el chatbot de salud mental[cite: 5].")
        st.write("Para 2025, el uso más común de la IA generativa ya es la búsqueda de apoyo emocional[cite: 6].")
    with col2:
        st.info("**Pregunta clave:** ¿Es una solución real o un experimento digital a gran escala? [cite: 7]")

# 3. Evolución (Tabs)
st.header("La metamorfosis del acompañante digital [cite: 8]")
t1, t2, t3 = st.tabs(["Fase 1", "Fase 2", "Fase 3"])

with t1:
    st.write("**Guiones rígidos:** Sistemas de reglas que funcionaban como contestadores automáticos[cite: 11].")
with t2:
    st.write("**Machine Learning:** Los bots empezaron a entender el tono mediante procesamiento de lenguaje natural (NLP)[cite: 14, 15].")
with t3:
    st.write("**LLMs (Actualidad):** Sistemas como ChatGPT y Gemini que generan lenguaje nuevo y coherente en tiempo real[cite: 16, 17].")

# 4. Evidencia Científica y Gráfico
st.header("¿Qué dice la ciencia? [cite: 19]")
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
    fig.update_layout(
        title="Eficacia de la IA (% de mejora)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color="white"),
        yaxis=dict(gridcolor='rgba(255,255,255,0.2)')
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.write("* **Universitarios:** Logran reducciones de hasta el 22% en síntomas depresivos[cite: 24].")
    st.write("* **Adultos Mayores:** Ayudan a combatir la soledad crónica y el aislamiento[cite: 25, 26].")
    st.write("* **Ansiedad:** Mejora promedio del 21% mediante reestructuración cognitiva[cite: 27].")

# 5. Riesgos (Expanders)
st.header("Las sombras y puntos ciegos [cite: 28, 30]")
with st.expander("Peligros de la IA"):
    st.write("* **Empatía artificial:** Puede crear una dependencia peligrosa al abandonar el contacto humano[cite: 32, 34].")
    st.write("* **Alucinaciones:** Riesgo de consejos médicos inventados con consecuencias fatales[cite: 35, 37].")
    st.write("* **Vacío legal:** Solo el 16% de las IAs avanzadas han pasado pruebas de eficacia clínica[cite: 38, 40].")

# 6. Conclusión y Niveles
st.divider()
st.subheader("Hacia una 'receta' digital segura [cite: 41]")
c1, c2, c3 = st.columns(3)
c1.metric("1. Validación", "Técnica [cite: 44]")
c2.metric("2. Pruebas", "de Usuario [cite: 45]")
c3.metric("3. Eficacia", "Clínica [cite: 46]")

st.write("> La profundidad de la psique humana sigue necesitando la comprensión de otro ser humano[cite: 48].")

# 7. Referencias
with st.expander("Ver Referencias Bibliográficas"):
    st.write("- Hua, Y., et al. (2024). World Psychiatry. [cite: 51]")
    st.write("- Nyakhar, S. & Wang, H. (2025). Front. Psychiatry. [cite: 52]")
    st.write("- Satake, Y., et al. (2026). Psychological Medicine. [cite: 53]")
    st.write("- Manole, A., et al. (2024). Information Journal. [cite: 54]")
    st.write("- Agencia SINC (2025). Alberto Payo. [cite: 55]")
