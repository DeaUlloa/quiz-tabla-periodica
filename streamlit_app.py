
import streamlit as st
import random

# Diccionario de elementos del 1 al 40
elementos = {
    "H": "Hidrogeno", "He": "Helio", "Li": "Litio", "Be": "Berilio", "B": "Boro",
    "C": "Carbono", "N": "Nitrogeno", "O": "Oxígeno", "F": "Fluor", "Ne": "Neon",
    "Na": "Sodio", "Mg": "Magnesio", "Al": "Aluminio", "Si": "Silicio", "P": "Fosforo",
    "S": "Azufre", "Cl": "Cloro", "Ar": "Argon", "K": "Potasio", "Ca": "Calcio",
    "Sc": "Escandio", "Ti": "Titanio", "V": "Vanadio", "Cr": "Cromo", "Mn": "Manganeso",
    "Fe": "Hierro", "Co": "Cobalto", "Ni": "Níquel", "Cu": "Cobre", "Zn": "Zinc",
    "Ga": "Galio", "Ge": "Germanio", "As": "Arsenico", "Se": "Selenio", "Br": "Bromo",
    "Kr": "Kripton", "Rb": "Rubidio", "Sr": "Estroncio", "Y": "Itrio", "Zr": "Circonio"
}

# Lista para manipulación
elementos_lista = list(elementos.items())

# Inicializar estado de sesión
if "preguntas_simbolo" not in st.session_state:
    st.session_state.preguntas_simbolo = random.sample(elementos_lista, 20)
    st.session_state.preguntas_nombre = random.sample(elementos_lista, 20)
    st.session_state.respuestas_simbolo = [""] * 20
    st.session_state.respuestas_nombre = [""] * 20
    st.session_state.mostrar_resultados = False

st.set_page_config(page_title="Quiz Tabla Periódica", page_icon="🔬")
st.title("🔬 Quiz Tabla Periódica (Elementos del 1 al 40)")
st.markdown("""
Este quiz contiene **40 preguntas** sobre los primeros elementos químicos de la tabla periódica.

- **20 preguntas sobre símbolos → nombre**
- **20 preguntas sobre nombres → símbolo**

¡Mucha suerte!
""")

with st.form("form_quimica"):
    st.subheader("🧪 Parte 1: ¿Cuál es el nombre del elemento con este símbolo?")
    for i, (simbolo, nombre) in enumerate(st.session_state.preguntas_simbolo):
        entrada = st.text_input(f"{i+1}. Símbolo: {simbolo}", value=st.session_state.respuestas_simbolo[i])
        st.session_state.respuestas_simbolo[i] = entrada

    st.subheader("🧪 Parte 2: ¿Cuál es el símbolo químico de este elemento?")
    for i, (simbolo, nombre) in enumerate(st.session_state.preguntas_nombre):
        entrada = st.text_input(f"{i+21}. Elemento: {nombre}", value=st.session_state.respuestas_nombre[i])
        st.session_state.respuestas_nombre[i] = entrada

    enviado = st.form_submit_button("✅ Ver Resultados")

# Evaluación de respuestas
if enviado:
    st.session_state.mostrar_resultados = True

if st.session_state.mostrar_resultados:
    aciertos = 0
    st.subheader("📊 Resultados")

    st.markdown("### Parte 1: Símbolo → Nombre")
    for i, (simbolo, nombre) in enumerate(st.session_state.preguntas_simbolo):
        respuesta = st.session_state.respuestas_simbolo[i].strip().lower()
        if respuesta == nombre.lower():
            st.success(f"{i+1}. {simbolo} = {nombre} ✅")
            aciertos += 1
        else:
            st.error(f"{i+1}. {simbolo} ≠ {respuesta or '(sin respuesta)'} ❌ — Correcto: {nombre}")

    st.markdown("### Parte 2: Nombre → Símbolo")
    for i, (simbolo, nombre) in enumerate(st.session_state.preguntas_nombre):
        respuesta = st.session_state.respuestas_nombre[i].strip().capitalize()
        if respuesta == simbolo:
            st.success(f"{i+21}. {nombre} = {simbolo} ✅")
            aciertos += 1
        else:
            st.error(f"{i+21}. {nombre} ≠ {respuesta or '(sin respuesta)'} ❌ — Correcto: {simbolo}")

    st.info(f"🏁 Puntuación final: **{aciertos} / 40** aciertos.")

# Botón de reinicio
import streamlit.components.v1 as components
if st.button("🔁 Actualizar"):
    components.html(
        "<script>window.location.reload();</script>",
        height=0,
        width=0
    )
