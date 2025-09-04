import streamlit as st

SDG_es_1 = """
    <div style="background-color:orange; padding: 25px; border-radius: 10px; text-align: center;">
        <h2 style="color:white;">Fin de la pobreza</h2>
        <a href="https://www.un.org/sustainabledevelopment/es/poverty/" target="_blank" style="color:white; font-size: 18px; text-decoration: underline;">
            Click aquí para saber más
        </a>
    </div>
    """

SDG_es_3 = """
    <div style="background-color:green; padding: 25px; border-radius: 10px; text-align: center;">
        <h2 style="color:white;">Salud y bienestar</h2>
        <a href="https://www.un.org/sustainabledevelopment/es/health/" target="_blank" style="color:white; font-size: 18px; text-decoration: underline;">
            Click aquí para saber más
        </a>
    </div>
    """

SDG_es_4 = """
    <div style="background-color:red; padding: 25px; border-radius: 10px; text-align: center;">
        <h2 style="color:white;">Educación de calidad</h2>
        <a href="https://www.un.org/sustainabledevelopment/es/education/" target="_blank" style="color:white; font-size: 18px; text-decoration: underline;">
            Click aquí para saber más
        </a>
    </div>
    """


def main():
    st.set_page_config(page_title="Metas ODS", page_icon="🌆")

    st.title("Metas de desarrollo sostenible")
    user_input = st.text_area("Brinda tus opiniones 🌐")

    if st.button("Analizar"):
        st.text("aaa")

    st.markdown("**Tu resultado es:**")
    st.markdown(SDG_es_1, unsafe_allow_html=True)
    st.markdown(SDG_es_3, unsafe_allow_html=True)
    st.markdown(SDG_es_4, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
