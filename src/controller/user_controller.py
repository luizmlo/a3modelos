import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from pages.login_professor import login_professor_view, login_professor_controller

def handle_user_selection():
    st.title("Bem-vindo ao sistema da SchoolTech!")
    navbar_options = ["Selecione a opção", "Aluno", "Professor"]
    selected_option = option_menu("Você é aluno ou professor?", navbar_options)
    if selected_option and selected_option != "Selecione a opção":
        page_mapping = {"Aluno": None, "Professor": "login professor"}
        page_name = page_mapping[selected_option]
        if page_name:
            switch_page(page_name)
            hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
            """
            st.markdown(hide_streamlit_style, unsafe_allow_html=True)
