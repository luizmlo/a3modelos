import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def show_login_page():
    st.header("Bem vindo ao sistema da SchoolTech!")
    st.subheader("Por favor, faça login para continuar.")
    username = st.text_input("Registro acadêmico")
    password = st.text_input("Senha", type="password")
    if st.button("Login"):
        return username, password
    return None, None

def show_login_success_message():
    st.success("Login realizado com sucesso!")

def show_login_error_message():
    st.error("Usuário ou senha incorretos!")

def hide_streamlit_footer():
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
