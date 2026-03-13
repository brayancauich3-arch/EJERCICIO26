import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="IA en Salud Mental",
    page_icon="🧠",
    layout="wide"
)

# Estilo minimalista con bordes redondeados (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stAlert {
        border-radius: 15px;
        border: 1px solid #e0e0e0;
    }
    .footer {
        text-align: left;
        color: #6c757d;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Título y Frase Motivadora
st.title("¿Un psicólogo en el bolsillo?")
st.subheader("La revolución (y los riesgos) de la IA en nuestra salud mental [cite: 1, 2]")

st.markdown('<p class="footer">"La tecnología puede ser el puente, pero el encuentro entre dos seres humanos seguirá siendo el destino." [cite: 3]</p>', unsafe_allow_html=True)
st.divider()

# 2. Introducción y Contexto
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        En un mundo con costos prohibitivos y esperas de meses, los chatbots de salud mental emergen como una nueva figura[cite: 5]. 
        Para 2025, el apoyo emocional se ha convertido en el uso más común de la IA generativa[cite: 6].
        """)
    with col2:
        st.info("**Dato Clave:** El uso emocional de la IA ya supera a las tareas laborales y creativas[cite: 6].")

# 3. La Metamorfosis (Línea de tiempo)
st.header("La metamorfosis del acompañante digital [cite: 8]")
tabs = st.tabs(["1. Guiones Rígidos", "2. Machine Learning", "3. Era de los LLM"])

with tabs[0]:
    st.write("**Sistemas de reglas:** Funcionaban como contestadores automáticos basados en palabras clave (ej. 'estoy triste')[cite: 11, 12].")
with tabs[1]:
    st.write("**Procesamiento de Lenguaje Natural (NLP):** Capacidad para identificar el tono y distinguir entre crisis o estrés[cite: 14, 15].")
with tabs[2]:
    st.write("**Modelos de Lenguaje Grandes (LLM):** Sistemas como ChatGPT que 'piensan' probabilísticamente para generar diálogos coherentes y humanos[cite: 16, 17, 18].")

# 4. Evidencia Científica (Gráficos)
st.header("¿Qué dice la ciencia sobre su efectividad? [cite: 19]")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Reducción de Síntomas")
    # Datos de los estudios mencionados
    data = {
        'Condición': ['Depresión (Universitarios)', 'Ansiedad (General)'],
        'Reducción (%)': [22, 21]
    }
    df = pd.DataFrame(data)
    fig = go.Figure(data=[
        go.Bar(name='Mejora', x=df['Condición'], y=df['Reducción (%)'], marker_color='#4A90E2')
    ])
    fig.update_layout(yaxis_title="Porcentaje de Mejora (%)", template="simple_white")
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    st.markdown("""
    * **Universitarios:** Un 35% sufre depresión y 39% ansiedad. La IA actúa como 'primer auxilio'[cite: 22, 23].
    * **Adultos Mayores:** Ayudan a reducir el aislamiento social y la depresión en personas sin deterioro cognitivo[cite: 25, 26].
    * **Ansiedad:** Mejora promedio del 21% mediante ejercicios de respiración y reestructuración cognitiva[cite: 27].
    """)

# 5. Riesgos y Sombras
st.header("Las Sombras: Riesgos Críticos [cite: 28]")
with st.expander("Ver advertencias éticas de la APA y Agencia SINC"):
    st.warning("**Simulación de Empatía:** La IA no siente, predice palabras. Esto puede generar dependencias peligrosas[cite: 32, 33, 34].")
    st.error("**Alucinaciones:** Datos inventados presentados como verdades. Un consejo médico erróneo podría ser fatal[cite: 35, 36, 37].")
    st.info("**Vacío Legal:** Solo el 16% de las IAs avanzadas han sido sometidas a pruebas de eficacia clínica real[cite: 39, 40].")

# 6. Conclusión: El Modelo de 3 Niveles
st.divider()
st.subheader("Hacia una 'receta' digital segura [cite: 41]")
c1, c2, c3 = st.columns(3)
c1.metric("Nivel 1", "Validación Técnica")
c2.metric("Nivel 2", "Pruebas de Usuario")
c3.metric("Nivel 3", "Eficacia Clínica")

st.write("> La IA no reemplazará a los psicólogos, pero los psicólogos que usen IA podrían ser el futuro[cite: 42].")

# 7. Referencias Bibliográficas (Botón desplegable)
with st.expander("📚 Referencias (Artículos citados)"):
    st.write("- **Hua, Y., et al. (2024).** Charting the evolution of artificial intelligence mental health chatbots[cite: 51].")
    st.write("- **Nyakhar, S. & Wang, H. (2025).** Effectiveness of AI chatbots on mental health in college students[cite: 52].")
    st.write("- **Satake, Y., et al. (2026).** Autonomous conversational agents for loneliness and depression in older people[cite: 53].")
    st.write("- **Manole, A., et al. (2024).** Harnessing AI in Anxiety Management[cite: 54].")
    st.write("- **Agencia SINC (2025).** Chatbots y salud mental: ¿solución accesible o experimento peligroso?[cite: 55].")
