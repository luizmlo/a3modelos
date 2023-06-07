import streamlit as st
from streamlit_option_menu import option_menu

def show_user_selection_page():
    st.title("Bem-vindo ao sistema da SchoolTech!")
    navbar_options = ["Selecione a opção", "Aluno", "Professor"]
    selected_option = option_menu("Você é aluno ou professor?", navbar_options)
    return selected_option
