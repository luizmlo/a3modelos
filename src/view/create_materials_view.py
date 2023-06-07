import streamlit as st

def show_create_materials_page(subject_names):
    st.title("Cadastro de Conteúdo")
    content_name = st.text_input("Nome do Conteúdo")
    selected_subject = st.selectbox("Matéria", subject_names)
    date = st.date_input("Data de Cadastro")
    description = st.text_area("Descrição do Conteúdo", height=200)
    if st.button("Cadastrar"):
        return content_name, selected_subject, date, description
    return None, None, None, None

def show_success_message():
    st.success("Conteúdo cadastrado com sucesso!")

def show_warning_message():
    st.warning("Por favor, preencha o nome do conteúdo.")
