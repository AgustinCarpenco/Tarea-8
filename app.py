import streamlit as st
import pandas as pd
from PIL import Image

# Configuración de la página (Opcional)
st.set_page_config(
    page_title="Mi Aplicación con Streamlit",
    page_icon="⚡",
    layout="centered"
)

def main():
    """Función principal de la app"""
    st.title("Ahora anda 🚀")
    
    # Texto de bienvenida
    st.write("Bienvenido a mi aplicación de Streamlit. Haz cambios en el código y verás la actualización en vivo. 😉")

    # Botón para forzar la recarga manualmente (por si la auto-recarga no funciona)
    if st.button("Recargar app"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
