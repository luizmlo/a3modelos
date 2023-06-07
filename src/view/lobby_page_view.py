import streamlit as st
from streamlit_option_menu import option_menu

def show_welcome_message():
    st.header("Bem-vindo professor!")
    st.write("O que você deseja fazer hoje?")

def show_navbar(options):
    selected_option = option_menu("Menu", options)
    return selected_option

def show_recent_contents(subjects):
    st.title("Conteúdos Recentes")
    selected_subject = st.selectbox("Filtrar por matéria", subjects)
    if st.button("Filtrar"):
        return selected_subject
    return None
